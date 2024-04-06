using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MembersC
{
    internal class Members
    {
        private string memberName;
        private string jobTitle;
        private int salary;
        public int age;

        public string JobTitle { 
            get 
            {
                return jobTitle;
            } 
            set 
            {
                jobTitle = value;
            }
        }

        public void Introducing(bool isFriend)
        {
            if (isFriend)
            {
                SharingPrivateInfo();
            }
            else
            {
                Console.WriteLine("Hi, my name is {0}, and my job title is {1}. I'm {2} years old.", memberName, jobTitle, age);
            }
        }

        private void SharingPrivateInfo()
        {
            Console.WriteLine("My salary is {0}", salary);
        }

        public Members()
        {
            age = 30;
            memberName = "Lucy";
            salary = 60000;
            jobTitle = "Developer";
            Console.WriteLine("Object created.");
        }

        ~Members()
        {
            Console.WriteLine("Deconstruction of Members object.");
            Debug.Write("Deconstruction of Members object.");
        }
    }
}
