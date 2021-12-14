using System;

namespace FactoryMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            // if we want to change logic, we only need to change the creator type to MP3PlayerCreator  
            // Everything else stays the same!
            ICreator creator = new SpeakerCreator();

            IMusicPlayerProduct product = creator.createProduct();
            product.PlayMusic();

            creator = new MP3PlayerCreator();

            product = creator.createProduct();
            product.PlayMusic();
        }
    }
}
