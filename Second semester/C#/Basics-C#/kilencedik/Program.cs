using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kilencedik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Tömb létrehozás --> felsoroljuk az elemeit
            // 3. elem 6. karakterét kell megkapni
            string[] nevek = { "Dezső", "Rozál", "Cziczvarek", "Béla", "Evelin" };
            Console.WriteLine(nevek[2].Substring(5,2));

            // 20 elemű tömb deklarálás
            int[] szamok = new int[20];
            // Tömb feltöltés
            for (int i = 0; i < 20; i++)
            {
                szamok[i] = i;
            }
            Console.WriteLine(szamok[5]);

            // Összegzés tétele
            int osszeg = 0;
            for (int i = 0; i < szamok.Length; i++)
            {
                osszeg += szamok[i];
            }
            Console.WriteLine(osszeg);
            Console.ReadKey();
        }
    }
}
