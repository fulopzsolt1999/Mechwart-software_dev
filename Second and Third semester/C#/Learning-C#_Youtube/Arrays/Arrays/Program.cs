internal class Program
{
    private static void Main(string[] args)
    {
        int[] nums = new int[10];
        for (int i = 0; i < nums.Length; i++)
        {
            nums[i] = i * i;
            //Console.WriteLine("Element {0} = {1}", i, nums[i]);
        }

        int counter = 0;
        foreach (var k in nums)
        {
            //Console.WriteLine("Element {0} = {1}", counter++, k);
        }

        // 2D array
        //Array2D();

        // 3D array
        //Array3D();

        // Jagged Array
        JaggedArray();
    }

    private static void Array2D()
    {

        int[,] array2D = new int[,]
        {
            { 1,2,3 },
            { 4,5,6 },
            { 7,8,9 }
        };

        for (int i = 0; i < array2D.GetLength(0); i++)
        {
            for (int j = 0; j < array2D.GetLength(1); j++)
            {
                Console.WriteLine("Array2D values are {0}", array2D[i, j]);
            }
        }

        Console.WriteLine("Central value is {0}", array2D[1, 1]);
    }

    private static void Array3D()
    {
        string[,,] array3D = new string[,,]
        {
            {
                {"000","001"},
                {"010","011"}
            },
            {
                {"100","101"},
                {"110","111"}
            }
        };
        Console.WriteLine("The value is {0}", array3D[1, 1, 0]);
    }

    private static void JaggedArray()
    {
        int[][] jaggedArray = new int[][]
        {
            new int[] { 1, 2, 3, 4, 5 },
            new int[] { 6, 7, 8, 9 }
        };

        for (int i = 0; i < jaggedArray.Length; i++)
        {
            for (int j = 0; j < jaggedArray[i].Length; j++)
            {
                Console.WriteLine("{0}", jaggedArray[i][j]);
            }
        }
    }
}