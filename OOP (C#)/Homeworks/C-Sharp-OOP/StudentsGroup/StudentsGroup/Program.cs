using System;
using System.Collections.Generic;

namespace StudentsGroup
{

    class Group
    {
        private string name;
        List<Student> students = new List<Student>();

        public Group(string name)
        {
            this.name = name;
        }

        public void AddStudent(Student s)
        {
            students.Add(s);
        }

        public void GetInfo()
        {
            Console.WriteLine("Group name is: {0}", name);
            Console.WriteLine("Group members are:");
            foreach (Student s in students)
            {
                Console.WriteLine(s.Name);
            }
        }

        public void GetFullInfo() 
        {
            Console.WriteLine("Group name is: {0}", name);
            foreach (Student s in students)
            {
                Console.WriteLine("name: {0}, state: {1}", s.Name, s.State);
            }
        }
    }

    abstract class Student
    {
        private string name;
        protected string state;
        public string Name
        {
            get { return name; }
            set { name = value; }
        }
        public string State 
        {
            get { return state; }
            set { state = value; }
        }

        public Student(string name) 
        {
            this.name = name;
            state = "";
        }
        public abstract void Study();
        public void Read() 
        {
            state += "Read ";
        }
        public void Write()
        {
            state += "Write ";
        }
        public void Relax() 
        {
            state += "Relax ";
        }
    }

    class BadStudent : Student 
    {
        public BadStudent(string name) : base(name)
        {
            State = "bad ";
        }
        public override void Study()
        {
            Relax();
            Relax();
            Relax();
            Relax();
            Read();
        }
    } 

    class GoodStudent : Student
    {
        public GoodStudent(string name) : base(name)
        {
            State = "good ";
        }
        public override void Study()
        {
            Read();
            Write();
            Read(); 
            Write();
            Relax();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Group g = new Group("K-27");
            BadStudent a = new BadStudent("Alice");
            GoodStudent b = new GoodStudent("Bob");
            a.Study();
            b.Study();
            g.AddStudent(a);
            g.AddStudent(b);
            Console.WriteLine("GetInfo output:");
            g.GetInfo();
            Console.WriteLine("GetFullInfo output:");
            g.GetFullInfo();
        }
    }
}
