using System;

namespace Decorator
{
    class Program
    {
        static void Main(string[] args)
        {
            FirTree firTree = new FirTree();
            Action<string> shineColor = (color) => Console.WriteLine("The garland shines! It's color is {0}!", color);
            Action<string> coolEffect = (effect) => Console.WriteLine("The garland has a cool effect! It can {0}!", effect);
            GarlandDecorator dec1 = new GarlandDecorator(firTree, shineColor, "red");
            GarlandDecorator dec2 = new GarlandDecorator(dec1, coolEffect, "raise its brightness when you are nearby");
            ToyDecorator dec3 = new ToyDecorator(dec2, "bear");
            dec3.Execute();
        }
    }
}
