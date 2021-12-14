using System;
using System.Collections.Generic;

namespace Figures
{
    abstract class Figure
    {
        public abstract double Area();
        public abstract double Perimeter();
    }
    class Square : Figure
    {
        private double side;
        public Square (int side)
        {
            this.side = side;
        }
        
        public override double Area()
        {
            return side * side;
        }


        public override double Perimeter()
        {
            return 4 * side;
        }
    }

    class Circle : Figure
    {
        private double radius;

        private const double PI = 3.1415;

        public Circle(double radius)
        {
            this.radius = radius;
        }
        public override double Area(){
        {
            return PI * radius * radius;
        }
        public override double Perimeter()
        {
            return 2 * PI * radius; 
        }
    }

    class Rectangle : Figure
    {
        private double side1;
        private double side2;

        public Rectangle (double side1, double side2)
        {
            this.side1 = side1;
            this.side2 = side2;
        }

        public override double Area()
        {
            return side1 * side2;
        }

        public override double Perimeter()
        {
            return 2 * (side1 + side2);
        }
    }

    class Triangle : Figure
    {
        private double side1;
        private double side2;
        private double side3;

        public Triangle(double side1, double side2, double side3)
        {
            this.side1 = side1;
            this.side2 = side2;
            this.side3 = side3;
        }

        public override double Area()
        {
            double p = (side1 + side2 + side3) / 2;
            return Math.Sqrt(p * (p - side1) * (p - side2) * (p - side3));
        }

        public override double Perimeter()
        {
            return side1 + side2 + side3;
        }
    }

    class Rhombus : Figure
    {
        private double side;
        private double angleRAD;

        public Rhombus (double side, double angleRAD)
        {
            this.side = side;
            this.angleRAD = angleRAD;
        }

        public override double Area ()
        {
            return side * side * Math.Sin(angleRAD);
        }

        public override double Perimeter()
        {
            return 4 * side;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Circle c = new Circle(5);
            Square s = new Square(10);
            Rhombus rh = new Rhombus(10, 0.785);
            Rectangle rect = new Rectangle(10, 20);
            Triangle t = new Triangle(3, 4, 5);
            Console.WriteLine(c.Area().ToString() + " " + c.Perimeter().ToString());
            Console.WriteLine(s.Area().ToString() + " " + s.Perimeter().ToString());
            Console.WriteLine(rh.Area().ToString() + " " + rh.Perimeter().ToString());
            Console.WriteLine(rect.Area().ToString() + " " + rect.Perimeter().ToString());
            Console.WriteLine(t.Area().ToString() + " " + t.Perimeter().ToString());
        }
    }
}
