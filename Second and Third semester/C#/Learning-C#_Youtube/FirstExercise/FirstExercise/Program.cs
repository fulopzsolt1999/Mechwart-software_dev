using FirstExercise;

class Program
{
    static void Main(string[] args)
    {
        // Create an object of my class
        // an instance of Human
        Human gizi = new Human();
        Human natalie = new Human("Natalie");
        Human michael = new Human("Michael", "Miller");
        Human sissy = new Human("Sissy", "Wagner", "blue");
        Human franzl = new Human("Franzl", "Müller", "green", 54);

        gizi.IntroduceMyself();
        natalie.IntroduceMyself();
        michael.IntroduceMyself();
        sissy.IntroduceMyself();
        franzl.IntroduceMyself();

        Console.ReadKey();
    }

    
}