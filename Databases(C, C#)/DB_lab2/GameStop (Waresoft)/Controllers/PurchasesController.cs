using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Waresoft.Controllers
{
    public class PurchasesController : Controller
    {
        private readonly WaresoftContext _context;

        public PurchasesController(WaresoftContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index(int id)
        {
            List<Purchase> purchases;
            List<Software> software;
            
            ViewBag.CustomerId = id;

            if (id == 0)
            {
                purchases = await _context.Purchases.Include(p => p.Customer).Include(p => p.Software).ToListAsync();
            }
            else
            {
                ViewBag.Customer = _context.Customers.Find(id).Email;
                purchases = await _context.Purchases.Where(p => p.CustomerId == id).Include(p => p.Software).ToListAsync();
            }

            foreach (var p in purchases)
            {
                software = await _context.Software.Where(s => s.Id == p.SoftwareId).Include(s => s.Developer).ToListAsync();
                p.Software = software[0];
            }

            return View(purchases);
        }

        public IActionResult Purchase(int softwareId, int devId)
        {
            FillViewBag(softwareId, devId);
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Purchase(Customer model, int softwareId, int devId)
        {
            var customer = await _context.Customers.FirstOrDefaultAsync(c => c.Email.Equals(model.Email));
            bool duplicate = customer == null ? false : _context.Purchases.Any(p => p.SoftwareId == softwareId && p.CustomerId == customer.Id);

            if (duplicate)
            {
                ModelState.AddModelError("Email", "Ви вже придбали цей продукт");
            }

            if (ModelState.IsValid)
            {                
                if (customer == null)
                {
                    customer = model;
                    await _context.Customers.AddAsync(customer);
                    await _context.SaveChangesAsync();
                }

                var purchase = new Purchase() { CustomerId = customer.Id, SoftwareId = softwareId, Date = DateTime.Now };
                await _context.Purchases.AddAsync(purchase);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index", "Software", new { id = devId, purchased = true });
            }

            FillViewBag(softwareId, devId);
            return View(model);
        }

        public void FillViewBag(int softwareId, int devId)
        {
            ViewBag.DevId = devId;
            ViewBag.SoftwareId = softwareId;
            ViewBag.Software = _context.Software.Find(softwareId).Name;
        }
    }
}