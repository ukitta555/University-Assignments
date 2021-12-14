using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Waresoft
{
    public partial class Customer
    {
        private const string ERR_REQ = "Поле необхідно заповнити";
        private const string RGX_EMAIL = @"\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\Z";

        public Customer()
        {
            Purchases = new HashSet<Purchase>();
        }

        public int Id { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [StringLength(50)]
        [Display(Name = "Ім\'я")]
        public string Name { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [StringLength(50)]
        [Display(Name = "Прізвище")]
        public string Surname { get; set; }

        [Required(ErrorMessage = ERR_REQ)]
        [StringLength(50)]
        [RegularExpression(RGX_EMAIL, ErrorMessage = "Введіть коректну електронну адресу")]
        [Display(Name = "Email")]
        public string Email { get; set; }

        public virtual ICollection<Purchase> Purchases { get; set; }
    }
}
