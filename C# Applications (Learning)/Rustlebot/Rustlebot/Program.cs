using System;   
using System.IO;
using SteamKit2;
using System.Threading;
namespace Rustlebot
{
    class Program
    {

        //Strongtyped data held in memory before client initialisaiton.
        static SteamClient steamClient;
        static CallbackManager callbackmanager;
        static SteamUser steamUser;
        static bool isRunning;
        static string user, pass;
        static string authcode;
        static SteamFriends steamFriends;


        //Is ran when the application starts, gets user auth details and contains Callback Manager which listens for and sends to SteamClient callbacks.
        static void Main(string[] args)
        {
            Console.WriteLine("Start-up service initialized");
            Console.Write("Updating list of available Steam servers (unhandled)...");
            SteamDirectory.Initialize().Wait();
            Console.Write("Successful.");

            //STEAMCLIENT//
            //Create our steamclient instance
            Console.WriteLine("Virtualising Steam Client.");
            steamClient = new SteamClient();
            Console.Write("Successful.");

            // CALLBACK MANAGER//
            //Create a callback manager (callbackmanager). The callback manager is responsible for routing callbacks to function calls (below
            Console.WriteLine("Creating Callback Manager to route Steam API callbacks to functions...");
            callbackmanager = new CallbackManager(steamClient);
            Console.Write("Successful.");
            Console.WriteLine("Setting steamUser handler to pass authentication.");
            // The steamuser handler is used for logging on after successfully connecting
            steamUser = steamClient.GetHandler<SteamUser>();
            Console.Write("Successful.");
            //The SteamFriends handler is used for interactions with the Steam Friends list after successfully logging in.
            steamFriends = steamClient.GetHandler<SteamFriends>();

            // CALLBACKS 
            //Register the callbacks we will use. The callback manager will loop through these and route the callbacks to the functions specified
            Console.WriteLine("Registering callbacks to callback manager."); //Tells the handler...
            callbackmanager.Subscribe<SteamClient.ConnectedCallback>(Steam_Connected);
            callbackmanager.Subscribe<SteamUser.UpdateMachineAuthCallback>(Steam_RequestMachineAuth); // What to do incase steam guard (requests machine auth).
            callbackmanager.Subscribe<SteamClient.DisconnectedCallback>(Steam_Disconnected);
            callbackmanager.Subscribe<SteamUser.LoggedOnCallback>(Steam_LoggedOn); // What to do if logged on
            callbackmanager.Subscribe<SteamUser.LoggedOffCallback>(Steam_LoggedOff); // What to do if logged off
            callbackmanager.Subscribe<SteamUser.AccountInfoCallback>(Steam_OnAccountInfo); //What to do if steam requests account information online status.
            callbackmanager.Subscribe<SteamFriends.FriendMsgCallback>(Steam_OnMessage); // What to do if a message is recieved general message of the day.
            Console.WriteLine("Successful");

            //Start application
            Console.WriteLine("Bootcheck completed. Starting application");
            isRunning = true;
            Console.WriteLine("Connecting to Steam...");
            //Get credentials
            Console.Write("\nAttempting to open connection to Steam with {0}\n", user);

            //Connect to Steam servers
            steamClient.Connect();
            //Get credentials
            Console.WriteLine("Connection successful. Please enter the username and password of the steam account you would like to connect to...\n");
            Console.Write("Username: ");
            user = Console.ReadLine();
            Console.Write("Password: ");
            pass = Console.ReadLine();
            //Callback manager: a handling loop which listens for calls subscribed / sends callbacks to the SteamAPI in the event of response (SteamClient/SteamUser/SteamFriends)

            Console.Write("Listening to Steam...\n");
            Console.WriteLine("Press ESC to exit the bot...\n");

            // Listens for callbacks and routes those callbacks to functions specified, exits on ESC

            do
            {
                while (!Console.KeyAvailable)
                {
                    callbackmanager.RunWaitCallbacks(TimeSpan.FromSeconds(1));
                }
            } while (Console.ReadKey(true).Key != ConsoleKey.Escape && isRunning != false);
        
            

            //If the while loop ends, so does our application.
            Console.WriteLine("The application will now terminate\nPress any key to continue...");
            Console.ReadKey();
            Environment.Exit(1);
        }


        //If connection succeeded to Steam...
        static void Steam_Connected(SteamClient.ConnectedCallback callback)
        {

            if (callback.Result != EResult.OK)
            {
                Console.WriteLine("Reached servers but unable to connect to Steam: {0}", callback.Result);

                isRunning = false;
                return;
            }

            Console.WriteLine("Connected to Steam! Logging in '{0}'...", user);
            //Create Steam Guard sentryHash
            byte[] sentryHash = null;
            //Does SentryHash exist?
            if (File.Exists("sentry.bin"))
            {
                byte[] sentryfile = File.ReadAllBytes("sentry.bin");
                sentryHash = CryptoHelper.SHAHash(sentryfile);
            }

            //Pass to Steamguard (steamguard will call OnMachineAuth)
            steamUser.LogOn(new SteamUser.LogOnDetails
            {
                Username = user,
                Password = pass,

                AuthCode = authcode,
                SentryFileHash = sentryHash,

            });

        }

        //If Steamguard, handles Steamguard auth...
        static void Steam_RequestMachineAuth(SteamUser.UpdateMachineAuthCallback callback)
        {
            Console.WriteLine("Updating Sentry File...");
            byte[] sentryHash = CryptoHelper.SHAHash(callback.Data);
            File.WriteAllBytes("sentry.bin", callback.Data);
            steamUser.SendMachineAuthResponse(new SteamUser.MachineAuthDetails
            {
                JobID = callback.JobID,
                FileName = callback.FileName,
                BytesWritten = callback.BytesToWrite,
                FileSize = callback.Data.Length,
                Offset = callback.Offset,
                Result = EResult.OK,
                LastError = 0,
                OneTimePassword = callback.OneTimePassword,
                SentryFileHash = sentryHash,
            });
            Console.WriteLine("Done.");
        }

        //If Disconnected from Steam, reconnect...
        static void Steam_Disconnected(SteamClient.DisconnectedCallback callback)
        {
            //AccountLogonDenied disconnects us from steam, so we need to reconnect which allows us to log in.
            Console.WriteLine("General disconnect exception. Retrying in 5 seconds...\n");
            Thread.Sleep(TimeSpan.FromSeconds(5));
            steamClient.Connect();
        }

        //If connection successful then LoggedOnCallback will be called, logon...
        static void Steam_LoggedOn(SteamUser.LoggedOnCallback callback)
        {
            if (callback.Result != EResult.OK)
            {

                // STEAMGUARD CHECK// 
                //Log on blocked by SteamGuard
                if (callback.Result == EResult.AccountLogonDenied)
                {
                    // If we recieve AccountLogonDenied or AccountLogonDeniedNoMailSent then the account we're logging into is SteamGuard protected.
                    Console.WriteLine("Unable to logon to Steam: This account is SteamGuard protected.");
                    Console.Write("Please provide a SteamGuard authentication token: ");
                    authcode = Console.ReadLine();
                    return; 
                }
                //Else if "eresult == notOK" and no steamguard, raise unable to logon general exception (since != EResult.OK)
                Console.WriteLine("Unable to logon to Steam: {0} / {1}", callback.Result, callback.ExtendedResult);
                isRunning = false;
                return;
            }
            // SUCCESSFUL LOGON//
            Console.WriteLine("Successfully logged on!");
            // We are now able to perform actions on Steam. So if you called "steamUser.LogOff();" below this would call Steam to logoff. However this will raise a general disconnect (because we are still stuck in the handlers loop)

        }

        //If connection successful then LoggedOffCallback is called, logoff...
        static void Steam_LoggedOff(SteamUser.LoggedOffCallback callback)
        {
            Console.WriteLine("Logged off of Steam: {0}", callback.Result);
        }


        //While handler listening to SteamUser, set persona states, send chat message...
        static void Steam_OnAccountInfo(SteamUser.AccountInfoCallback callback)
        {   //SetPersonaState from the AccountInfo callback to Online (displays user as online).
            steamFriends.SetPersonaState(EPersonaState.Online);
        }

        //While handler is listening to SteamFriends return...
        static void Steam_OnMessage(SteamFriends.FriendMsgCallback callback)
        {   
            steamFriends.SendChatMessage(callback.Sender, EChatEntryType.ChatMsg, "Thank you for playing in the Rustlemania: Team USA v. Team EU will begin at 07/07/2016.");
        }
    }


}