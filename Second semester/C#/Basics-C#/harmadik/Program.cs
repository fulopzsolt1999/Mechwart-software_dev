using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace harmadik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("ADjon meg egy számot: ");
            double inp = double.Parse(Console.ReadLine());
            if (-10 < inp && inp < 10)
            {
                Console.Write($"A megadott {inp} szám 1 számjegyű.");
            }else if (-100 < inp || 100 > inp)
            {
                Console.Write($"A megadott {inp} szám 2 számjegyű.");
            } else if (-1000 < inp || 1000 > inp)
            { 
                Console.Write($"A megadott {inp} szám 3 számjegyű.");
            } else { Console.Write($"A megadott {inp} szám több mint 3 számjegyű."); }

            
            Console.ReadKey();
        }
    }
}
