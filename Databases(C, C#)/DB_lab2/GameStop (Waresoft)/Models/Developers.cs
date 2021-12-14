using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Waresoft
{
    public partial class Developer
    {
        private const string ERR_REQ = "Поле необхідно заповнити";

        public Developer()
        {
            Software = new HashSet<Software>();
        }

        public int Id { get; set; }

        [Display(Name = "Країна")]
        public int CountryId { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [StringLength(50)]
        [Display(Name = "Ім\'я/назва")]
        public string Name { get; set; }

        [Display(Name = "Країна")]
        public virtual Country Country { get; set; }
        public virtual ICollection<Software> Software { get; set; }
    }
}
