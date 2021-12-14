using System;

namespace Composite
{
    class Program
    {
        static void Main(string[] args)
        {
            // manager
            Person p1 = new Person(12);
            // programmers
            Person p2 = new Person(34);
            Person p3 = new Person(10);
            // CEO
            Person p4 = new Person(120);

            // manager group
            Composite comp1 = new Composite();
            comp1.Add(p1);
            // programming group
            Composite comp2 = new Composite();
            comp2.Add(p2);
            comp2.Add(p3);

            // employee level
            Composite comp3 = new Composite();
            comp3.Add(comp1);
            comp3.Add(comp2);
            // CEO level
            Composite comp4 = new Composite();
            comp4.Add(comp3);
            comp4.Add(p4);
            // calculate company workers' profits
            Console.WriteLine("company workers' profits: {0}", comp4.Execute());
        }
    }
}
