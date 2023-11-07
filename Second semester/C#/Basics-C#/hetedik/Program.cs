using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace hetedik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Számoljuk meg hogy 1M-ig hány db szám osztható 17-el

            //lassan megoldva

            /*int countSlow = 0;
            for (int i = 0; i < 1000000; i++)
            {
                if (i%17==0)
                {
                    countSlow++;
                }
            }
            Console.WriteLine(countSlow);

            //gyorsan megoldva
            int countFast = 0;
            for (int i = 17; i < 1000000; i+=17)
            {
                countFast++;
            }
            Console.WriteLine(countFast);
            */

            // Prím szám kereső
            // Akkor prím szám ha csak 1el és önmagával osztható

            int[] list = {2, 3, 4, 5, 6, 7, 8, 9};
            int prim = 0;
            int count = 0;
            for (int i = 11; i < 1000; i+=2)
            {
                for (int j = 0; j < list.Length; j++)
                {
                    if (i % list[j] != 0)
                    {
                        count++;
                    }
                }
                if (count % list.Length == 0)
                {
                    prim++;
                }
                count = 0;
            }
            Console.WriteLine(prim);

            Console.ReadKey();
        }
    }
}
