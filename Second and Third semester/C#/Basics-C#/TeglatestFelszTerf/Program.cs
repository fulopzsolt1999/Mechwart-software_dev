using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TeglatestFelszTerf
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Téglatest 3 oldala bekér, felszín és térfogat számítás
            Console.Write("Add meg a téglatest a oldalát: ");
            double a = double.Parse(Console.ReadLine());
            Console.Write("Add meg a téglatest b oldalát: ");
            double b = double.Parse(Console.ReadLine());
            Console.Write("Add meg a téglatest c oldalát: ");
            double c = double.Parse(Console.ReadLine());

            Console.WriteLine($"A téglatest térfogata: {Math.Round(a*b*c, 2)},\n" +
                $"A téglatest térfogata: {Math.Round(2*(a*b+b*c+a*c), 2)}");

            Console.ReadKey();
        }
    }
}
