using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Properties
{
    internal class Box
    {
        // Member variables
        private int length;
        private int height;
        //private int width;
        private int volume;
        public int Width { get; set; }

        public int Length
        {
            get
            {
                return length;
            }
            set
            { 
                this.length = value;
            }
        }

        public int Height
        {
            get
            {
                return height;
            }
            set
            {
                if (value < 0)
                {
                    height = -value;
                }
                else
                {
                    this.height = value;
                }
            }
        }

        public int Volume
        {
            get
            {
                return this.length* this.Width * this.height;
            }
            
        }

        public Box(int length, int height, int width)
        {
            this.length = length;
            this.height = height;
            Width = width;
        }

        public void DisplayInfo()
        {
            Console.WriteLine("Length: {0}, Height: {1}, Width: {2}, Volume: {3}", Length, Height, Width, Volume);
        }
    }
}
