using EU;

List<Csatlakozas> adatok = new List<Csatlakozas>();
foreach (string sor in File.ReadAllLines("EUcsatlakozas.txt"))
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
Console.WriteLine($"3. Feladat.\n\tAz EU tagállamainak száma: {adatok.Count} db");

int db = 0;

foreach (var i in adatok)
{
    if (i.Idopont.Year == 2007)
    {
        db++;
    }    
}
Console.WriteLine($"4. Feladat.\n\t2007-ben ennyien csatlakoztak: {db} db");

foreach (var item in adatok)
{
    if (item.Nev.Contains("Magyarorsz"))
    {
        Console.WriteLine($"5. Feladat.\n\tMagyarország csatlakozásának dátuma: {item.Idopont.ToString("yyyy.MM.dd")}");
    }   
}

Console.WriteLine("Add meg egy hónap számát: ");
int monthInput = Convert.ToInt32(Console.ReadLine());
bool checkMayJoin = false;
foreach (var item in adatok)
{
    if (item.Idopont.Month == monthInput)
    {
        checkMayJoin = true;
    }
}
if (checkMayJoin)
{
    Console.WriteLine($"6. Feladat.\n\tTörtént csatlakozás a megadott {monthInput} hónapban.");
}
else
{
    Console.WriteLine($"6. Feladat.\n\tNem történt csatlakozás a megadott {monthInput} hónapban.");
}

int index = 0;
var latestJoin = adatok[0].Idopont;
for (int i = 0; i < adatok.Count; i++)
{
    if (adatok[i].Idopont > latestJoin)
    {
        index = i;
        latestJoin = adatok[i].Idopont;
    }
}
Console.WriteLine($"7. Feladat.\n\tA leutoljára csatlakozott ország: {adatok[index].Nev}");

SortedSet<int> evek = new SortedSet<int>();

foreach (var i in adatok)
{
    evek.Add(i.Idopont.Year);
}

// most két ciklust egymásba ágyazva megkeressük,
// hogy az adott év hányszor fordul elő a fájlban
Console.WriteLine("8. Feladat.");
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

    Console.WriteLine($"\t{i} - {darab} ország");
}