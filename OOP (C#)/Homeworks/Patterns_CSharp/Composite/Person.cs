using System;
using System.Collections.Generic;
using System.Text;

namespace Composite
{
    class Person : IComponent
    {
        private int value;
        public Person(int value) 
        {
            this.value = value;
        }
        public int Execute() 
        {
            return value; 
        }
    }
}
