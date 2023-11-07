using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Tizedik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
            // 6 nap hőmérsékletét, hányszor csökkent a hő, hányszor fagyott
            int[] temp = new int[6];
            int fagy = 0;
            int hidegebb = 0;
            for (int i = 0; i < 6; i++)
            {
                Console.WriteLine($"Adja meg milyen idő volt {6-i} napja");
                temp[i] = int.Parse(Console.ReadLine());
            }

            for (int i = 0; i < temp.Length; i++)
            {
                if (i+1 != temp.Length)
                {
                    if (temp[i] <= 0)
                    {
                        Console.WriteLine($"A(z) {i+1}. napon fagy volt.");
                        fagy++;
                    }
                    if (temp[i + 1] < temp[i])
                    {
                        Console.WriteLine($"A(z) {i+1}. napról a(z) {i + 2}. napra lehülés volt.");
                        hidegebb++;
                    }
                }
            }
            Console.WriteLine($"Hőmérsékletek: {temp}");
            Console.WriteLine($"Ennyiszer volt lehülés: {hidegebb}");
            Console.WriteLine($"Ennyiszer volt fagy: {fagy}");
            Console.ReadKey();
        }
    }
}
