using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Basics_Project_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //KIÍRÓ UTASÍTÁS
            Console.WriteLine("Hello World!");
            Console.WriteLine("Szia!");
            Console.WriteLine("    Harmadik sor");
            //Kiírás azonos sorba
            Console.Write("Egyforma ");
            Console.Write("sor.");
            //Ez így rossz, sort kell dobni előtte
            Console.WriteLine("Meglepi");
            //nézzük meg jó
            //kezdjünk egy üres sorral
            Console.WriteLine();
            Console.Write("Egyforma ");
            //beszúrunk egy sortörést \n
            Console.Write("sor.\n");
            Console.WriteLine("Meglepi");
            //VÁLTOZÓK!!!
            //MINDNEK VAN TÍPUSA!!!
            //típus : változó neve : esetlegesen változó értéke

            int x;
            x = 6;
            Console.WriteLine(2 * x);
            //a változó csak azt a típust tartalmazhatja
            //x = "Dezső";
            //x=6,5; a C# a tizedes az PONT!!!
            //x = 6.5; lebegőpontos és nem INT!!!
            string vezetek, kereszt;
            vezetek = "Tóth";
            kereszt = "Dezső";
            //Írjuk ki, hogy Szia Kedves Tóth Dezső!
            //Kiírás első módja
            Console.WriteLine("Szia Kedves " + vezetek + " " + kereszt + "!");
            //Második módszer Python f sztring!!!
            Console.WriteLine($"Szia Kedves {vezetek} {kereszt}!");

            //BEOLVASÁS
            Console.Write("Add meg a vezetékneved: ");
            vezetek = Console.ReadLine();
            Console.Write("Add meg a keresztneved: ");
            kereszt = Console.ReadLine();
            Console.WriteLine($"Szia Kedves {vezetek} {kereszt}!");
            //olvassunk be számokat

            Console.WriteLine("Adj meg egy számot: ");
            int z = int.Parse(Console.ReadLine());
            Console.WriteLine($"Ez a szám: {z}");
            //Kérjük be egy téglalap 2 oldalát és írjuk ki a területét, kerületét
            Console.Write("Add meg az a oldalt: ");
            int a = int.Parse(Console.ReadLine());
            Console.Write("Add meg a b oldalt: ");
            int b = int.Parse(Console.ReadLine());
            int terulet = a * b;
            int kerulet = 2 * (a + b);
            Console.WriteLine($"A téglalap területe: {terulet} a kerülete: {kerulet}");
            Console.WriteLine($"Terület: {a * b} Kerület: {2 * a + 2 * b}");
            //Adott egy henger alakú hordó, átmérője 1m magassága 2m Hány liter bor fér bele?
            //Első lépés: a henger TÉRFOGATA KELL!
            //2. lépés 1m^3 = ?l => 1m^3=1000l
            //3. Térfogat = ALAPTERÜLET * MAGASSÁG
            //4. Kör területe: r^2 * PÍ
            double r = 0.5;
            double t = r * r * 3.14;
            double v = t * 2;
            Console.WriteLine($"A hordóba: {1000 * v} liter bor fér");

            Console.Write("Add meg az átmérőt: ");
            double atm = double.Parse(Console.ReadLine());
            Console.Write("Add meg a magasságot: ");
            double mag = double.Parse(Console.ReadLine());
            double r1 = atm / 2;
            double t1 = r1 * r1 * 3.14;
            double v1 = t1 * mag;
            Console.WriteLine($"A hordóba: {1000 * v1} liter bor fér");
            // Ha igazi aranyból lenne az aranylabda (5-ös fociméret) akkor Messi fel bírná-e emelni?
            //Hány kg? A lebda kerülete 69,5 cm
            //OSZTÁSI VÉSZHELYZET!!!
            //EGÉSZ SZÁMOK ESETÉN A / EGÉSZ OSZTÁST JELENT!!!!

            //Mennyi az 5/8

            int x3 = 5;
            int y3 = 8;
            Console.WriteLine(x3 / y3);

            Console.ReadKey();
        }
    }
}
