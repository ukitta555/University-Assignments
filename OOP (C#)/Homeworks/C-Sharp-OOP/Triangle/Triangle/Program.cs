
using System;

namespace Triangle
{
    class InvalidValueException : Exception
    {
        public InvalidValueException (string message) : base(message)
        {

        }
    }

    class UnsupportedOperationException : Exception
    {
        public UnsupportedOperationException(string message) : base(message)
        {

        }
    }
    class Triangle
    {
        protected double ab;
        protected double bc;
        protected double ac;

        private bool checkNegativity (double value)
        {
            return (value < 0);
        }

        private bool checkTriangleInequality (double side1, double side2, double side3)
        {
            return ((side1 <= side2 + side3) && (side1 >= Math.Abs(side2 - side3)));
        }
        public void SetAB (double value)
        { 
            try
            {
                if (checkNegativity(value) || !checkTriangleInequality (value, bc, ac))
                {
                    throw new InvalidValueException("Triangle inequality not satisfied / value is negative!");
                }
                ab = value;
            }
            catch (InvalidValueException e)
            {
                Console.WriteLine("InvalidValueException: {0}", e.Message);
            }
        }

        public  void SetBC(double value)
        {
            try
            {
                if (checkNegativity(value) || !checkTriangleInequality(value, ab, ac))
                {
                    throw new InvalidValueException("Triangle inequality not satisfied / value is negative!");
                }
                bc = value;
            }
            catch (InvalidValueException e)
            {
                Console.WriteLine("InvalidValueException: {0}", e.Message);
            }
        }

        public void SetAC (double value)
        {
            try
            {
                if (checkNegativity(value) || !checkTriangleInequality(value, bc, ab))
                {
                    throw new InvalidValueException("Triangle inequality not satisfied / value is negative!");
                }
                ac = value;
            }
            catch (InvalidValueException e)
            {
                Console.WriteLine("InvalidValueException: {0}", e.Message);
            }
        }
        public  Triangle(double ab, double bc, double ac)
        {
            this.ab = ab;
            this.bc = bc;
            this.ac = ac;
            try
            {
                if (checkNegativity(ab) || checkNegativity(bc) || checkNegativity(ac))
                {
                    throw new InvalidValueException("Negative values!");
                }
                if (!checkTriangleInequality(ab, bc, ac) || !checkTriangleInequality(bc, ac, ab) || !checkTriangleInequality(ac, bc, ab))
                {
                    throw new InvalidValueException("Triangle inequality not satisfied!");
                }
            }
            catch (InvalidValueException e)
            {
                Console.WriteLine("InvalidValueException: {0}", e.Message);
            }
        }

        public double AngleABAC()
        {
            return Math.Acos((ab * ab + ac * ac - bc * bc) / (2 * ab * ac));
        }
        public double AngleABBC()
        {
            return Math.Acos((ab * ab + bc * bc - ac * ac) / (2 * ab * bc));
        }
        public double AngleACBC()
        {
            return Math.Acos((ac * ac + bc * bc - ab * ab) / (2 * ac * bc));
        }

        public double Perimeter()
        {
            return ab + bc + ac;
        }
    }
    class Equilateral : Triangle
    {
        private double area;

        public Equilateral(double ab, double ac, double bc) : base (ab, ac, bc)
        {
            try
            {
                if (ab != ac || ac != bc)
                {
                    throw new InvalidValueException("Sides should be equal!");
                }
            }  catch (InvalidValueException e)
            {
                Console.WriteLine("InvalidValueException: {0}", e.Message);
            }
            SetAB(ab);
            SetAC(ac);
            SetBC(bc);
            }
        public double Area()
        {
            area = ab * ab * Math.Sqrt(3) / 4;
            return area;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Triangle t = new Triangle(1, 2, Math.Sqrt(5));
            Console.WriteLine(t.AngleABAC());
            Console.WriteLine(t.AngleABBC());
            Console.WriteLine(t.AngleACBC());
            t.SetAB(3);
            t.SetBC(4);
            t.SetAC(5);
            Console.WriteLine(t.AngleABAC());
            Console.WriteLine(t.AngleABBC());
            Console.WriteLine(t.AngleACBC());
        }
    }
}
