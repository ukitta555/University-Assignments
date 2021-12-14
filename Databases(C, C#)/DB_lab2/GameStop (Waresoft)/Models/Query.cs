using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Waresoft.Models
{
    public class Query
    {
        public string QueryId { get; set; }

        public string Error { get; set; }

        public int ErrorFlag { get; set; }

        public string DevName { get; set; }

        public string CountryName { get; set; }

        public decimal AvgPrice { get; set; }

        public List<string> CustNames { get; set; }

        public List<string> CustSurnames { get; set; }

        public List<string> CustEmails { get; set; }

        public List<string> ProdNames { get; set; }

        public List<decimal> ProdPrices { get; set; }

        public string CustName { get; set; }

        public string CustSurname { get; set; }

        public string CustEmail { get; set; }

        public List<string> DevNames { get; set; }

        public List<DateTime> Dates { get; set; }

        [Required(ErrorMessage = "Поле необхідно заповнити")]
        [RegularExpression(@"^[0-9]+(\.[0-9]{1,2})?$", ErrorMessage = "Введіть коректну вартість")]
        [Display(Name = "Вартість В")]
        public decimal Price { get; set; }

        [Required(ErrorMessage = "Поле необхідно заповнити")]
        [RegularExpression(@"^[0-9]+$", ErrorMessage = "Введіть коректне число")]
        [Display(Name = "Число продуктів N")]
        public decimal Number { get; set; }

        [Required(ErrorMessage = "Поле необхідно заповнити")]
        public string ProdName { get; set; }

        public int DevId { get; set; }

        public List<string> CountryNames { get; set; }
    }
}
