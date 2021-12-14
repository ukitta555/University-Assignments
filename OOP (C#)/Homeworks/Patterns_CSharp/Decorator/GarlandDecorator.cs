using System;
using System.Collections.Generic;
using System.Text;

namespace Decorator
{
    class GarlandDecorator : BaseDecorator
    {
        private Action<string> garlandAction;
        string what;
        public GarlandDecorator(IComponent component, Action<string> action, string what) : base (component) 
        {
            garlandAction = action;
            this.what = what;
        }
        

        public override void Execute()
        {
            garlandAction(what);
            base.Execute();
        }
    }
}
