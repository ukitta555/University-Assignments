using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod
{
    class MP3PlayerCreator : ICreator
    {
        public IMusicPlayerProduct createProduct() 
        {
            return new MP3Player();
        }
    }
}
