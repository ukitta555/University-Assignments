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
    public class DevelopersController : Controller
    {
        private const string ERR_DEV_EXISTS = "Введений розробник вже доданий";
        private readonly WaresoftContext _context;

        public DevelopersController(WaresoftContext context)
        {
            _context = context;
        }

        // GET: Developers
        public async Task<IActionResult> Index()
        {
            return View(await _context.Developers.Include("Country").ToListAsync());
        }

        // GET: Developers/Details/5
        public async Task<IActionResult> Details(int id)
        {
            var software = await _context.Software.Where(s => s.DeveloperId == id).Include("Comments").ToListAsync();
            ViewBag.Developer = _context.Developers.Find(id).Name;
            return View();
        }

        // GET: Developers/Create
        public IActionResult Create()
        {
            ViewBag.CountryList = new SelectList(_context.Countries.ToList(), "Id", "Name");
            return View();
        }

        // POST: Developers/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(Developer developer)
        {
            bool duplicate = await _context.Developers.AnyAsync(d => d.Name.Equals(developer.Name));

            if (duplicate)
            {
                ModelState.AddModelError("Name", ERR_DEV_EXISTS);
            }

            if (ModelState.IsValid)
            {
                _context.Add(developer);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }

            ViewBag.CountryList = new SelectList(_context.Countries.ToList(), "Id", "Name");
            return View(developer);
        }

        // GET: Developers/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            var developers = await _context.Developers.FindAsync(id);
            ViewBag.CountryList = new SelectList(_context.Countries.ToList(), "Id", "Name");
            return View(developers);
        }

        // POST: Developers/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(Developer developer)
        {
            bool duplicate = await _context.Developers.AnyAsync(d => d.Name.Equals(developer.Name) && d.CountryId == developer.CountryId && d.Id != developer.Id);

            if (duplicate)
            {
                ModelState.AddModelError("Name", ERR_DEV_EXISTS);
            }

            if (ModelState.IsValid)
            {
                _context.Update(developer);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }

            ViewBag.CountryList = new SelectList(_context.Countries.ToList(), "Id", "Name");
            return View(developer);
        }

        // POST: Developers/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var developers = await _context.Developers.FindAsync(id);
            _context.Developers.Remove(developers);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }
    }
}
