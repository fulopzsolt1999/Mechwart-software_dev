using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CelsiusToFaren
{
    internal class Program
    {
        public void weather(string cOrF, double n)
        {

        }
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write("°C vagy °F?: ");
                string celOrFar = Console.ReadLine();
                Console.Write("Hány fok van?: ");
                double num = double.Parse(Console.ReadLine());
                if (celOrFar == "c" || celOrFar == "C" || celOrFar == "°C")
                {
                    weather("C", num);
                    Console.Write($"Ez fahreinheit-ben ennyi(°F): {Math.Round(num * 1.8 + 32)}");
                    break;
                }
                else if (celOrFar == "f" || celOrFar == "F" || celOrFar == "°F")
                {
                    Console.Write($"Ez fahreinheit-ben ennyi(°F): {Math.Round((num - 32) / 1.8)}");
                    break;
                }
                else
                {
                    Console.Write("!!!c/C/°C vagy f/F/°F!!!");
                }
            }
            
            Console.ReadKey();
        }
    }
}
