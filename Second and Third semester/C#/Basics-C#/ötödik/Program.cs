using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace otodik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // kétjegyű 7-el osztható számok
            for (int i = 10; i < 100; i++)
            {
                if (i % 7 == 0)
                {
                    Console.WriteLine(i);
                }
            }

            for (int i = 14; i < 100; i += 7)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine("**************");
            for (int i = 'A'; i <= 'Z'; i++)
            {
                Console.WriteLine((char)i);
            }
            //írjunk ki 20 véletlen számot 0-1000 között
            Random r = new Random();
            for (int i = 0; i < 20; i++)
            {
                Console.WriteLine(r.Next(1001));
            }
            // írjunk ki lottószámokat ötöt 1-90

            Random kismacska = new Random();
            for (int i = 0; i < 5; i++)
            {
                int x = kismacska.Next(1, 91);
                Console.WriteLine(x);
            }

            // Generáljunk 10 számot rosszul
            Random b = new Random();

            int t = b.Next(1, 1001);

            for (int i = 0; i < 20; i++)
            {
                t++;
                Console.WriteLine(t);
            }
            // Generáljunk 10 számot 1-100 között és 
            // írjuk ki a legnagyobbat, legkisebbet, átlagot
            int szam;
            int legnagyobb = 0, legkisebb = 100, osszeg = 0;
            for (int i = 0; i < 10; i++)
            {
                szam = b.Next(1, 101);
                // legkisebb megkeresése
                if (szam < legkisebb)
                {
                    legkisebb = szam;
                }

                if (szam > legnagyobb)
                {
                    legnagyobb = szam;
                }
                osszeg = osszeg + szam; // osszeg += szam

            }

            Console.WriteLine($"Kicsi: {legkisebb} Nagy: {legnagyobb} Átlag: {osszeg / (double)10}");

            // Számoljuk ki, hogy mennyi 1-től 10-ig a számok szorzata

            int szorzat = 1;
            for (int i = 1; i < 11; i++)
            {
                szorzat = szorzat * i;
            }

            Console.WriteLine(szorzat);


            // Számoljuk ki a 9-el osztható 4 jegyű számok átlagát
            osszeg = 0;
            double db = 0;
            for (int i = 1000; i < 10000; i++)
            {
                if (i % 9 == 0)
                {
                    db++; // db +=1; db = db + 1
                    osszeg = osszeg + i;
                }
            }
            Console.WriteLine($"A 9-el osztható 4 jegyű számok átlaga: {osszeg / db}");
            // ciklusok egymásba ágyazása
            // kérjünk be egy oldalhosszt, majd *-ból rajzoljunk egy ekkora négyzetet
            Console.Write("Add meg az oldalhosszt: ");
            int oldal = int.Parse(Console.ReadLine());

            // Először a külső ciklusba lép, majd lefut a TELJES belső ciklus
            // utána a külső ciklus lép egyet és újra lefut a TELJES belső ciklus
            // és így tovább

            for (int j = 0; j < oldal; j++) //  külső ciklus
            {

                for (int i = 0; i < oldal; i++) // belső ciklus
                {
                    Console.Write('*');
                }
                Console.WriteLine();

            }

            // Próbáljuk meg kiírni a szorzótáblát.

            Console.ReadKey();

        }
    }
}