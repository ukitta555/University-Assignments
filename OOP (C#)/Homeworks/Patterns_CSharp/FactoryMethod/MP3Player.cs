using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod
{
    class MP3Player : IMusicPlayerProduct
    {
        public void PlayMusic() 
        {
            Console.WriteLine("MP3 player plays music with medium volume using headphones.");
        }
    }
}
