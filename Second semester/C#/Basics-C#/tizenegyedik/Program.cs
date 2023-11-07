using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tizenegyedik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // beolvas név, keresztnév kiirat
            Console.WriteLine("Adja meg a nevét");
            string name = Console.ReadLine();
            string keresztnev = "";
            for (int i = 0; i < name.Length; i++)
            {
                if (name[i] == ' ')
                {
                    i++;
                    keresztnev = name.Substring(i, name.Length-i);
                    break;
                }
            }
            Console.WriteLine(keresztnev);

            // 5 név tömbben, vizsgáljuk olyat ad e meg ami benne van vagy nicns
            string[] nevek = { "Zoli", "Gyula", "Sanyi", "Zsolti", "Béla" };
            Console.WriteLine("Adjon meg egy keresztnevet");
            if (nevek.Contains(Console.ReadLine()))
            {
                Console.WriteLine("Benne van gratulálok.");

            }
            else
            {
                Console.WriteLine("Nincs benne te szar.");
            }

            // input egy mondat, hány karakter, hány szó, 4. szó, 2. szó 4. karakter
            Console.WriteLine("Adjon meg egy mondatot:");
            string mondat = Console.ReadLine();
            Console.WriteLine(mondat);
            int space = 0;
            int space_3 = 0;
            int space_4 = 0;
            for (int i = 0; i < mondat.Length; i++)
            {
                if (mondat[i] == ' ')
                {
                    space++;
                    if (space == 1)
                    {
                        Console.WriteLine($"Második szó 4. karaktere: {mondat.Substring(i+4, 1)}");
                    }
                    if (space == 3)
                    {
                        space_3 = i+1;
                    }
                    if (space == 4)
                    {
                        space_4 = i - space_3;
                    }
                }
            }
            Console.WriteLine($"Ennyi karakter szóköz nélkül: {mondat.Length-space}");
            Console.WriteLine($"Ennyi szó van: {space+1}");
            Console.WriteLine($"A 4. szó: {mondat.Substring(space_3, space_4)}");

            Console.ReadKey();
        }
    }
}
