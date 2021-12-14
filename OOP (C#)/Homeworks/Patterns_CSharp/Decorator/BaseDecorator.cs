using System;
using System.Collections.Generic;
using System.Text;

namespace Decorator
{
    class BaseDecorator : IComponent
    {
        IComponent wrapee;
        public BaseDecorator(IComponent component) 
        {
            wrapee = component;
        }

        public virtual void Execute() 
        {
            wrapee.Execute();
        }
    }
}
