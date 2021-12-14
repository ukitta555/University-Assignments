using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Waresoft
{
    public partial class Country
    {
        public Country()
        {
            Developers = new HashSet<Developer>();
        }

        public int Id { get; set; }

        [Required(ErrorMessage = "Поле необхідно заповнити")]
        [StringLength(50)]
        public string Name { get; set; }

        public virtual ICollection<Developer> Developers { get; set; }
    }
}
