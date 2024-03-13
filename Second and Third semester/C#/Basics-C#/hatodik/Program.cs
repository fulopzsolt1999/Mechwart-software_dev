using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hatodik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Kérjünk be egy számot és írjuk ki, hogy 
            // osztható-e 3-al és 4-el
            // vagy csak 3-al, de 4-el nem
            // vagy csak 4-el, de 3-al nem
            // vagy egyikkel sem

            /* másik feladat: pénzfeldobást szimulálunk
             véletlenül előállítunk 0-át vagy 1-et
             100000-szer és megnézzük az arányukat. 
            (0-ák száma osztva az 1-ek számával)
            Ha tényleg véletlenek a számok, akkor 
            ez az arány közel lesz 1-hez! */

            Console.Write("Adj meg egy számot: ");
            int x = int.Parse(Console.ReadLine());
            if (x % 3 == 0 && x % 4 == 0)
            {
                Console.WriteLine("3-al és 4-el");
            }
            else if (x % 3 == 0 && x % 4 != 0)
            {
                Console.WriteLine("3-al de 4-el nem");
            }
            else if (x % 3 != 0 && x % 4 == 0)
            {
                Console.WriteLine("3-al nem de 4-el igen");
            }
            else
            {
                Console.WriteLine("egyikkel sem osztható");
            }

            Random r = new Random();
            int egyesek_db = 0;
            int nullasok_db = 0;
            for (int i = 0; i < 100000; i++)
            {
                int veletlenszam = r.Next(2);
                if (veletlenszam == 0)
                {
                    nullasok_db++;
                }
                else
                {
                    egyesek_db++;
                }
            }
            Console.WriteLine($"Az arány: {nullasok_db / (double)egyesek_db}");

            //Írj programot, mely beolvas egy pozitív
            //egész számot, és kiírja az osztóit!

            //Írj programot, mely beolvas egy pozitív egész számot,
            //és megmondja, hogy tökéletes szám-e!
            //(A tökéletes számok azok, melyek
            //osztóinak összege egyenlő a
            //szám kétszeresével.
            //Ilyen szám pl.a 6, mert 2 * 6 = 1 + 2 + 3 + 6.)

            //Kérjünk be egy max. 3 jegyű számot
            //és döntsük el, hogy prímszám-e?

            Console.Write("Adj meg egy számot: ");
            int oszthato = int.Parse(Console.ReadLine());
            int tokeletes = 0;
            for (int i = 1; i <= oszthato; i++)
            {
                if (oszthato % i == 0)
                {
                    tokeletes = tokeletes + i;
                    Console.WriteLine($"Ennek a számnak: {oszthato} osztója ez a szám: {i}");

                }
            }
            //a ciklus lefutása után a tokeletes változó tartalmazza az osztók összegét

            if (oszthato * 2 == tokeletes)
            {
                Console.WriteLine($"A {oszthato} szám tökéletes");
            }

            int db = 0;

            for (int i = 1; i <= oszthato; i++)
            {
                if (oszthato % i == 0)
                {
                    db++;
                }
            }
            if (db == 2)
            {
                Console.WriteLine("prím");
            }


            // NEM előírt lépésszámú ciklus!!! WHILE
            // nagyon könnyű VÉGTELEN CIKLUST ÍRNI!!!
            // A szintaktika: WHILE logikai vizsgálat
            // A ciklus magja
            // Addig fut, amíg a logikai vizsgálat értéke IGAZ
            // Ezt ELÖLTESZTELŐ ciklusnak hívjuk
            // Lehet, hogy EGYSZER SEM FUT LE!!!

            // Írjunk programot, ami 1-10-ig kiírja a számokat
            // FOR ciklussal
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine(i + 1);
            }
            // WHILE ciklussal
            int ciklusvaltozo = 1;
            while (ciklusvaltozo < 11)
            {
                Console.WriteLine(ciklusvaltozo);
                ciklusvaltozo++;
            }

            //írjunk végtelen ciklust
            /*
            int sr = 1;
            while (true)
            {
                
                Console.WriteLine( $"{sr}. Dezső");
                sr++;
            }*/
            //A WHILE ciklus belsejében változtatni kell a ciklusváltozót
            // írjunk olyan WHILE ciklust, ami egyszer sem fut le

            int t = 10;
            while (t < 6)
            {
                Console.WriteLine("Béla");
            }

            string jelszo = "Bela";

            while (jelszo != "Dezső")
            {
                Console.Write("Add meg a jelszót: ");
                jelszo = Console.ReadLine();
            }
            Console.WriteLine("Köszöntelek kedves felhasználó!");
            //Kérjünk be egy 3-al osztható páros számot
            //és csak akkor menjünk tovább, ha ilyet írt be a felhasználó

            //Írj programot, ami csak
            //pozitív számot hajlandó beolvasni.

            bool be = true;

            while (be)
            {
                Console.Write("Írj be 3-al osztható páros számot: ");
                int beolvas = int.Parse(Console.ReadLine());
                if (beolvas % 3 == 0 && beolvas % 2 == 0)
                {
                    be = false;
                }
            }
            Console.WriteLine("Jó számot adtál meg!");

            be = true;
            while (be)
            {
                Console.Write("Írj be egy pozitív számot: ");
                int pozitiv = int.Parse(Console.ReadLine());
                if (pozitiv > 0)
                {
                    be = false;
                }
            }
            Console.WriteLine("Gratulálunk, ügyes vagy Kedves Dezső!");
            // HÁTULTESZTELŐ CIKLUS
            //EGYSZER MINDENKÉPP LEFUT!
            // AMIT MEG LEHET OLDANI AZ EGYIKKEL
            //AZT MEG LEHET OLDANI A MÁSIKKAL IS!!
            // EGYENÉRTÉKŰEK!!!

            // ha tehetjük, akkor a WHILE ciklust használjuk!

            // DO ... WHILE (logikai vizsgálat)
            //Írjunk cilust, ami 1-10-ig kiírja a számokat
            int p = 1;
            do
            {
                Console.WriteLine(p);
                p++;
            } while (p < 11);
            // Hátultesztelő ciklussal írjunk 
            // jelszóvekérő programot
            // a jelszó legyen Rozál


            Console.ReadKey();

        }
    }
}