using System;

// Liskov substituion principle was violated.

interface IRect
{
    int Width { get; set; }
    int Height { get; set; }
    int GetRectangleArea();
}

interface ISquare 
{
    int Side { get; set; }
    int GetSquareArea();
}
class Rectangle : IRect
{
    public int Width { get; set; }
    public int Height { get; set; }
    public int GetRectangleArea()
    {
        return Width * Height;
    }
}

//квадрат наслідується від прямокутника!!!
class Square : ISquare
{
    public int Side { get; set; }
    
    public int GetSquareArea() { return Side * Side; }
    class Program
    {
        static void Main(string[] args)
        {
            Square square = new Square();
            square.Side = 5;

            Console.WriteLine(square.GetSquareArea());
            Console.ReadKey();
        }
    }
}