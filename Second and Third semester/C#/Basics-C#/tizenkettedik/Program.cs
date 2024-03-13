using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tizenkettedik
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // lottó szám sorsolás
            Console.WriteLine("Adja meg a legnagyobb kihúzható számot.");
            int max_num = int.Parse(Console.ReadLine());
            Console.WriteLine("Adja meg hány számot szeretne.");
            int pull_num = int.Parse(Console.ReadLine());

            Random random = new Random();
            List<int> rnums = new List<int>();
            int rnum = 0;

            for (int i = 0; i < pull_num; i++)
            { 
                while (true)
                {
                    rnum = random.Next(1, max_num+1);
                    if (!rnums.Contains(rnum))
                    {
                        rnums.Add(rnum);
                        break;
                    }
                }
                if (rnums.Count == max_num)
                {
                    break;
                }
            }
            rnums.Sort();
            for (int i = 0; i < rnums.Count; i++)
            {
                Console.WriteLine(rnums[i]);
            }

            // 2018 május informatika érettségi 4. feladat
            string sourceFile = "C://Users//fulop//Desktop//Mechwart-software_dev//Second semester//C#//Basics-C#//tizenkettedik//ajto.txt";
            string targetFile = "C://Users//fulop//Desktop//Mechwart-software_dev//Second semester//C#//Basics-C#//tizenkettedik//Athaladas.txt";
            List<List<string>> sourceData = new List<List<string>>();
            int firstIn = 0;
            int lastOut = 0;
            try
            {
                string[] lines = File.ReadAllLines(sourceFile);

                foreach (var line in lines)
                {
                    string[] szavak = line.Split(' ');
                    List<string> sorLista = new List<string>();
                    sourceData.Add(sorLista);
                }

                /*for (int i = 0; i < sourceData.Count; i++)
                {
                    if (sourceData[i][4].ToString() == "be")
                    {
                        firstIn = sourceData[i][3];
                    } 
                }
                for (int i = sourceData.Count; i > 0; i--)
                {
                    if (sourceData[i][4].ToString() == "ki")
                    {
                        lastOut = sourceData[i][3];
                    }
                }*/
            }
            catch (Exception err)
            {
                Console.WriteLine("Hiba történt: " + err.Message);
            }
            finally
            {
                
                Console.WriteLine($"Első érkező: {firstIn}\nUtolsó távozó: {lastOut}");
            }
            Console.ReadKey();
        }
    }
}
