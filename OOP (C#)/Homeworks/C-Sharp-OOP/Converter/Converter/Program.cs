using System;

namespace Converter
{
    class NonpositiveException : Exception 
    {
        public NonpositiveException(string message) : base(message) {}
    }
    class Converter
    {
        private double usdPrice;
        private double euroPrice;

        public double USDPrice
        {
            get { return usdPrice; }
            set 
            {
                try
                {
                    if (value > 0) usdPrice = value;
                    else throw new NonpositiveException("Price can't be nonpositive!");
                }
                catch (NonpositiveException e)
                {
                    Console.WriteLine("Exception caught:{0}", e.Message);
                }
            }
        }

        public double EURPrice
        {
            get { return euroPrice; }
            set 
            {
                try
                {
                    if (value > 0) euroPrice = value;
                    else throw new NonpositiveException("Price can't be nonpositive!");
                }
                catch (NonpositiveException e) 
                {
                    Console.WriteLine("Exception caught:{0}", e.Message);
                }


            }
        }

        // 1 USD = usdPrice UAH, 1 EUR = euroPrice UAH
        public Converter(double usdPrice, double euroPrice)
        {
            USDPrice = usdPrice;
            EURPrice = euroPrice;
        }

        public double UAHtoUSD(double uahAmount)
        {
            try
            {
                if (uahAmount < 0) throw new NonpositiveException("Amount should be a positive number!");
                return uahAmount / usdPrice;
            }
            catch (NonpositiveException e)
            {
                Console.WriteLine("Exception caught:{0}", e.Message);
                return -1;
            }
        }

        public double USDtoUAH(double usdAmount)
        {
            try
            {
                if (usdAmount < 0) throw new NonpositiveException("Amount should be a positive number!");
                return usdAmount * usdPrice;
            }
            catch (NonpositiveException e)
            {
                Console.WriteLine("Exception caught:{0}", e.Message);
                return -1;
            }
            
        }
        public double UAHtoEUR(double uahAmount)
        {
            try
            {
                if (uahAmount < 0) throw new NonpositiveException("Amount should be a positive number!");
                return uahAmount / euroPrice;
            }
            catch (NonpositiveException e) 
            {
                Console.WriteLine("Exception caught:{0}", e.Message);
                return -1;
            }
        }

        public double EURtoUAH (double eurAmount) 
        {
            try
            {
                if (eurAmount < 0) throw new NonpositiveException("Amount should be a positive number!");
                return eurAmount * euroPrice;
            }
            catch (NonpositiveException e)
            {
                Console.WriteLine("Exception caught:{0}", e.Message);
                return -1;
            }
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Converter converter = new Converter(28, 30);
            Console.WriteLine (converter.EURtoUAH(30));
            Console.WriteLine (converter.UAHtoEUR(1000));
            Console.WriteLine (converter.UAHtoUSD(2800));
            Console.WriteLine(converter.USDtoUAH(500));
            // bad tests! (throw exception for negative values) !!!!
            Converter badConverter = new Converter(-28, -30);
            Console.WriteLine(converter.USDtoUAH(-123));

        }
    }
}
