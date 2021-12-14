using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Waresoft
{
    public partial class Purchase
    {
        public int Id { get; set; }
        public int CustomerId { get; set; }
        public int SoftwareId { get; set; }

        [Display(Name = "Дата покупки")]
        public DateTime Date { get; set; }

        public virtual Customer Customer { get; set; }
        public virtual Software Software { get; set; }
    }
}
