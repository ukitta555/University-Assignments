using System;

namespace Triangle2
{
    abstract class Triangle
    {
        protected double side1;
        protected double side2;
        protected double angleRAD;
        protected const double PI = 3.1415;
        public abstract double Area();
        public abstract double Perimeter();
    }

    class RightTriangle : Triangle
    {

        public RightTriangle(double side1, double side2)
        {
            this.side1 = side1;
            this.side2 = side2;
            angleRAD = PI / 2;
        }
        public override double Area()
        {
            return side1 * side2 / 2;
        }

        public override double Perimeter()
        {
            return side1 + side2 + Math.Sqrt(side1 * side1 + side2 * side2);
        }
    } 

    class IsoscelesTriangle : Triangle
    {
        public IsoscelesTriangle (double side1, double side2, double angleRAD)
        {
            this.side1 = side1;
            this.side2 = side2;
            this.angleRAD = angleRAD;
        }

        public override double Perimeter()
        {
            return 2 * side1 + side2;
        }

        public override double Area()
        {
            return side1 * side2 * Math.Sin(angleRAD) / 2;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            IsoscelesTriangle it = new IsoscelesTriangle(4, 8, 0.87);
            RightTriangle rt = new RightTriangle(3, 4);
            Console.WriteLine(it.Area().ToString() + " " + it.Perimeter().ToString());
            Console.WriteLine(rt.Area().ToString() + " " + rt.Perimeter().ToString());
        }
    }
}
