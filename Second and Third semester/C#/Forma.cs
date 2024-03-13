using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_Forma1
{
    internal class Forma
    {
        public string Datum { get; set; }
        public string Nagydij { get; set; }
        public int Helyezes { get; set; }
        public int Kor { get; set; }
        public int Pont { get; set; }
        public string Csapat { get; set; }
        public string Statusz { get; set; }



        // Kétfajta módra hozunk létre konstruktort
        // Első esetben a fájl egy sorát az osztályban daraboljuk fel
        // tehát paraméternek a konstruktor egyetlen sort kap

        public Forma(string sor)
        {
            string[] darabka = sor.Split(';');
            Datum = darabka[0];
            Nagydij = darabka[1];
            Helyezes = int.Parse(darabka[2]);
            Kor = int.Parse(darabka[3]);
            Pont = int.Parse(darabka[4]);
            Csapat = darabka[5];
            Statusz = darabka[6];
        }

        public Forma(string datum, string nagydij, int helyezes, int kor, int pont, string csapat, string statusz)
        {
            Datum = datum;
            Nagydij = nagydij;
            Helyezes = helyezes;
            Kor = kor;
            Pont = pont;
            Csapat = csapat;
            Statusz = statusz;
        }
    }
}
