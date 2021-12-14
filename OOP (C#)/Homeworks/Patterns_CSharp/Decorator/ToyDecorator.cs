using System;
using System.Collections.Generic;
using System.Text;

namespace Decorator
{
    class ToyDecorator : BaseDecorator
    {
        string toy = "";
        public ToyDecorator (IComponent component, string toy) : base (component) 
        {
            this.toy = toy;
        }
        public override void Execute()
        {
            Console.WriteLine("That's a toy on a tree! It's a {0}!", toy);
            base.Execute();
        }
    }
}
