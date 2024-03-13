using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EU
{
    internal class Csatlakozas
    {
        public string Nev { get; set; }
        //NEM így tároljuk a dátumot, hanem kihasználjuk a C# beépített típusait
        // melyek segítségével sokkal könnyebb a munka a dátumokkal, időkkel
        // ezeket most nem fogjuk használni, de itt maradnak, hogy lássuk a folyamatot
        
        public int Ev { get; set; }
        public int Ho { get; set; }
        public int Nap { get; set; }
        
        public DateTime Idopont { get; set; }

        public Csatlakozas(string sor)
        {
            string[] resz = sor.Split(';');
            Nev = resz[0];
            Idopont = Convert.ToDateTime(resz[1]);
            
            //ezt alul NEM fogjuk használni
            string[] bontottdatum = resz[1].Split('.');
            Ev = int.Parse(bontottdatum[0]);
            Ho = int.Parse(bontottdatum[1]);
            Nap = int.Parse(bontottdatum[2]);
            
        }


    }
}
