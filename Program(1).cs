using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EU
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Csatlakozas> adatok = new List<Csatlakozas>();
            foreach(string sor in File.ReadAllLines("Eucsatlakozas.txt"))
            {
                // a beolvasás kifejtve 2 sorban, először példányosítunk
                // és csak utána adjuk hozzá a listához
                /*
                Csatlakozas x = new Csatlakozas(sor);
                adatok.Add(x);
                */

                // ha egyetlen sorban akarom ezt kiírni
                adatok.Add(new Csatlakozas(sor));
            }
            Console.WriteLine($"Az EU tagállamainak száma: {adatok.Count} db");
            // Írjuk ki Ausztria csatlakozásának dátumát, az indexe: 0-a
            Console.WriteLine(adatok[0].Idopont);

            //2007-ben csatlakozott országok száma
            int db = 0;
            foreach (var i in adatok)
            {
                if (i.Idopont.Year== 2007)
                {
                    db++;
                }
            }
            Console.WriteLine($"2007-ben ennyien csatlakoztak: {db} db");

            foreach (var i in adatok)
            {
                if (i.Nev.Contains("Magy"))
                {
                    //Console.WriteLine($"Magyarország csatlakozásának a dátuma: {i.Ev}.{i.Ho}.{i.Nap}");
                    Console.WriteLine($"Magyarország csatlakozásának a dátuma: {i.Idopont.ToString("yyyy.MM.dd")}");

                }
            }

            bool volt = false;
            foreach (var i in adatok)
            {
                if (i.Idopont.Month==5)
                {
                    volt = true;
                    break;
                }
            }

            if (volt)
            {
                Console.WriteLine("Volt csatlakozás májusban");
            }
            else
            {
                Console.WriteLine("Nem volt csatlakozás májusban");

            }
            // ki csatlakozott utoljára?
            // felvesszük a mai napot, igazából a MOST-ot
            DateTime now = DateTime.Now;
            TimeSpan elteltido = now - adatok[0].Idopont;
            // Ezzel kiszámoljuk, hogy hány nap telt el a csatlakozás óta
            double minimum = elteltido.TotalDays;
            int ind = 0;
            for (int i = 0; i < adatok.Count; i++)
            {
                if ((now - adatok[i].Idopont).TotalDays < minimum)
                {
                    ind = i;
                    minimum = (now - adatok[i].Idopont).TotalDays;
                }
            }
            Console.WriteLine($"A leutoljára csatlakozott ország: {adatok[ind].Nev}");
            // A megszokott statisztika
            // először kigyűjtjük az éveket
            // halmazba, hogy egyediek legyenek

            SortedSet<int> evek = new SortedSet<int>();

            foreach (var i in adatok)
            {
                evek.Add(i.Idopont.Year);
            }

            // most két ciklust egymásba ágyazva megkeressük,
            // hogy az adott év hányszor fordul elő a fájlban

            foreach (var i in evek)
            {
                int darab = 0;
                foreach (var j in adatok)
                {
                    if (i == j.Idopont.Year)
                    {
                        darab++;
                    }
                }

                Console.WriteLine($"{i} - {darab} ország");

            }





            Console.ReadKey();

        }
    }
}
