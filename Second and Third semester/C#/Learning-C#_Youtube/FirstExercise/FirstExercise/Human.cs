using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FirstExercise
{
    // This class is a blueprint for a datatype
    class Human
    {
        // Member variable
        private string firstName;
        private string lastName;
        private string eyeColor;
        private int age;

        public Human()
        {
            Console.WriteLine("Constructor called, Object created!");
        }

        public Human(string firstName)
        {
            this.firstName = firstName;
        }

        public Human(string firstName, string lastName)
        {
            this.firstName = firstName;
            this.lastName = lastName;

        }

        public Human(string firstName, string lastName, string eyeColor)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.eyeColor = eyeColor;
        }

        // Parameterized Constructor
        public Human(string firstName, string lastName, string eyeColor, int age)
        {
            this.firstName = firstName;
            this.lastName = lastName;
            this.eyeColor = eyeColor;
            this.age = age;
        }

        // Member method
        public void IntroduceMyself()
        {
            if (firstName != null && lastName != null && eyeColor != null && age != 0)
            {
                Console.WriteLine("Hi, My name is {0} {1}, I have {2} eyes, I'm {3} year old.", firstName, lastName, eyeColor, age);
            } else if (firstName != null && lastName != null && eyeColor != null)
            {
                Console.WriteLine("Hi, My name is {0} {1}, I have {2} eyes.", firstName, lastName, eyeColor);
            } else if (firstName != null && lastName != null)
            {
                Console.WriteLine("Hi, My name is {0} {1}.", firstName, lastName);
            } else if (firstName != null)
            {
                Console.WriteLine("Hi, My name is {0}.", firstName);
            }
        }
    }
}
