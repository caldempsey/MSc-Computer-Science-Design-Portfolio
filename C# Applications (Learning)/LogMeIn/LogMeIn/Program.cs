using System;
namespace Learning
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome. The purpose of this application is to show how I code!\n");
            Console.WriteLine("Please enter your name...");
            string personName = Console.ReadLine();
            Console.WriteLine("\nHello, " + personName + "\n");
            bool allowedAccess = verificationCheck();
        }
        public static bool verificationCheck()
        {
            string logonPW = "Test123";
            string pwProvided = "";
            int logonAttempt = 0;
            Console.WriteLine("Please enter the password...");
            pwProvided = Console.ReadLine();
            while (logonAttempt < 5)
            {
                if (pwProvided == logonPW)
                {
                    Console.WriteLine("\nCorrect, Welcome to the app! Happy learning!\nPlease press any key to exit the application.");
                    Console.ReadKey();
                    return true;
                }
                else
                {
                    Console.WriteLine("\nAccess Denied. Try again!\n");
                    logonAttempt++;
                    Console.WriteLine("You have used " + logonAttempt + " out of 5 attempts!");
                    Console.WriteLine("Please try enter the password again...");
                    pwProvided = Console.ReadLine();
                }
            }
            return false;
        }
    }
}