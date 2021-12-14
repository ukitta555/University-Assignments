using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Waresoft
{
    public partial class Software
    {
        private const string ERR_REQ = "Поле необхідно заповнити";

        public Software()
        {
            Purchases = new HashSet<Purchase>();
        }

        public int Id { get; set; }

        [Display(Name = "Розробник")]
        public int DeveloperId { get; set; }
        
        [Required(ErrorMessage = ERR_REQ)]
        [StringLength(50)]
        [Display(Name = "Назва")]
        public string Name { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [RegularExpression(@"^[0-9]+(\.[0-9]{1,2})?$", ErrorMessage = "Введіть коректну вартість")]
        [Display(Name = "Вартість")]
        public decimal Price { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [Display(Name = "Опис")]
        public string Description { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [Display(Name = "Системні вимоги")]
        public string Requirements { get; set; }

        [Display(Name = "Розробник")]
        public virtual Developer Developer { get; set; }
        public virtual ICollection<Purchase> Purchases { get; set; }
    }
}
