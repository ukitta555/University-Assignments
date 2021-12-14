using System;
using System.Collections.Generic;
using System.Text;

namespace FactoryMethod
{
    interface ICreator
    {
        IMusicPlayerProduct createProduct();
    }
}
