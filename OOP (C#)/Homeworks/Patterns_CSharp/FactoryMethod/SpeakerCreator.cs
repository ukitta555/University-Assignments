using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod
{
    class SpeakerCreator : ICreator
    {
        public IMusicPlayerProduct createProduct() 
        {
            return new Speakers();
        }
    }
}
