using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod
{
    class Speakers : IMusicPlayerProduct
    {
        public void PlayMusic()
        {
            Console.WriteLine("Speakers play music loudly.");
        }
    }
}
