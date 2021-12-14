using System;
using System.Collections.Generic;
using System.Text;

namespace Composite
{
    class Composite : IComponent
    {
        List<IComponent> components;

        public Composite()
        {
            this.components = new List<IComponent>();
        }

        public Composite(List<IComponent> components) 
        {
            this.components = components;
        }

        public void Add (IComponent componentToAdd) 
        {
            components.Add(componentToAdd);
        }

        public int Execute() 
        {
            int sum = 0;
            foreach (IComponent child in components)
            {
                sum += child.Execute();
            }
            return sum;
        }
    }
}
