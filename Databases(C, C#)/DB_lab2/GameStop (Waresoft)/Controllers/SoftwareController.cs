using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using Waresoft;

namespace Waresoft.Controllers
{
    public class SoftwareController : Controller
    {
        private const string ERR_SOFT_EXISTS = "Такий продукт вже доданий";
        private readonly WaresoftContext _context;

        public SoftwareController(WaresoftContext context)
        {
            _context = context;
        }

        // GET: Software
        public async Task<IActionResult> Index(int id, bool purchased)
        {
            List<Software> software;
            ViewBag.DevId = id;
            
            if (purchased)
            {
                ViewBag.Purchased = 1;
            }

            if (id == 0)
            {
                software = await _context.Software.Include(s => s.Developer).ToListAsync();
            }
            else
            {
                ViewBag.Developer = _context.Developers.Find(id).Name;
                software = await _context.Software.Where(s => s.DeveloperId == id).Include(s => s.Developer).ToListAsync();
            }

            return View(software);
        }

        // GET: Software/Create
        public IActionResult Create(int devId)
        {
            ViewBag.DevId = devId;
            if (devId != 0)
            {
                ViewBag.Developer = _context.Developers.Find(devId).Name;
            }
            ViewBag.DeveloperList = devId == 0 ?
            new SelectList(_context.Developers, "Id", "Name") :
            new SelectList(new List<Developer>() { _context.Developers.Find(devId) }, "Id", "Name");
            return View();
        }

        // POST: Software/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(Software software)
        {
            ViewBag.DevId = software.DeveloperId;
            ViewBag.Developer = _context.Developers.Find(software.DeveloperId).Name;

            bool duplicate = _context.Software.Any(s => s.DeveloperId == software.DeveloperId && s.Name.Equals(software.Name));

            if (duplicate)
            {
                ModelState.AddModelError("Name", ERR_SOFT_EXISTS);
            }

            if (ModelState.IsValid)
            {
                _context.Add(software);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index", new { id = software.DeveloperId });
            }

            ViewBag.DeveloperList = new SelectList(_context.Developers, "Id", "Name", software.DeveloperId);
            return View(software);
        }

        // GET: Software/Edit/5
        public async Task<IActionResult> Edit(int id, int devId)
        {
            var software = await _context.Software.FindAsync(id);
            ViewBag.DevId = devId;
            ViewBag.DeveloperList = new SelectList(_context.Developers, "Id", "Name", software.DeveloperId);
            return View(software);
        }

        // POST: Software/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(Software software, int devId)
        {
            ViewBag.DevId = devId;
            bool duplicate = _context.Software.Any(s => s.Id != software.Id && s.DeveloperId == software.DeveloperId && s.Name.Equals(software.Name));

            if (duplicate)
            {
                ModelState.AddModelError("Name", ERR_SOFT_EXISTS);
            }

            if (ModelState.IsValid)
            {
                _context.Update(software);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index), new { id = devId });
            }

            ViewBag.DeveloperList = new SelectList(_context.Developers, "Id", "Name", software.DeveloperId);
            return View(software);
        }

        // POST: Software/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var software = await _context.Software.FindAsync(id);
            _context.Software.Remove(software);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }
    }
}
