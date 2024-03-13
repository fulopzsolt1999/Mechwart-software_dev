using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_Forma1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Forma> adatok = new List<Forma>();
            // itt a beolvasandó fájl sorain
            // lépkedek végig
            // Az első sort KIHAGYJUK A BEOLVASÁSBÓL!!!
            foreach (var sor1 in File.ReadAllLines("schumacher.csv").Skip(1))
            {
                Forma x = new Forma(sor1);
                
                adatok.Add(x);
            }

            Console.WriteLine(adatok[9].Nagydij);

            // Ha bonyolult a fájl felépítése, akkor itt
            // szoktuk feldarabolni és úgy hívjuk
            // a konstruktort

            // ebben az esetben beolvassuk a teljes
            // fájlt egy sztring típusú tömbbe

            List<Forma> adatok1 = new List<Forma>();

            string[] beolvas = File.ReadAllLines("schumacher.csv");

            for (int i = 1; i < beolvas.Length; i++)
            {
                string[] resz = beolvas[i].Split(';');
                string d = resz[0];
                string n = resz[1];
                int h = int.Parse(resz[2]);
                int k = int.Parse(resz[3]);
                int p = int.Parse(resz[4]);
                string cs = resz[5];
                string st = resz[6];
                Forma x = new Forma(d,n, h, k, p, cs, st);
                adatok1.Add(x);
            }

            Console.WriteLine(adatok1[9].Nagydij);

            //Harmadik feladat, a fájlban hány sor van?
            Console.WriteLine(adatok.Count);
            Console.WriteLine("A magyar nagydíj helyezései:");
            foreach (var i in adatok)
            {
                if (i.Helyezes !=0 && i.Nagydij.Contains("ungar"))
                {
                    Console.WriteLine($"{i.Datum}: {i.Helyezes}. hely");
                }
            }
            // létrehozunk egy halmazt, amiben minden csak egyszer marad benne
            HashSet<string> hiba1 = new HashSet<string>();
            // létrehozunk egy olyan halmazt, amiben minden ABC sorrendben marad

            SortedSet<string> hiba = new SortedSet<string>();

            foreach (var i in adatok)
            {
                if (i.Helyezes==0)
                {
                    hiba.Add(i.Statusz);
                }
            }
            // kigyűjtjük, melyik hiba HÁNYSZOR FORDULT ELŐ

            int db = 0;
            foreach (var i in hiba)
            {
                
                foreach (var j in adatok)
                {
                    if (j.Statusz == i)
                    {
                        db++;
                    }
                }
                if (db > 2)
                {
                    Console.WriteLine($"{i}: {db}");
                }
            }



            Console.ReadKey();
        }
    }
}
