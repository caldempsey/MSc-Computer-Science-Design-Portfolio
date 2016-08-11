__author__ = 'MMACheerpuppy'

print ("Rustlemania Matchmaking Service")
print ("*"*45)
print ("")
print ("Initializing engine.")
engine_error = 0

### GLOBS WE WILL NEED ###

while True:
    try:
        print ("Writing arrays into memory")
        player_usernames = []
        player_ranks = []
        player_steamurls = []
        processed_ranks = []
        player_powerlevels = []
        powerlevel_database = []
        calculated_powerlevels = []
        rank_database = []
        badplayer_position = []
        goodplayer_position = []
        player_assignedteams = []
        no_playerranks = 0
        filename = ("")
        no_playerranks = 0
        adjusted_player_powerlevels = []
        isfilemounted = True
        teamsbuilt = False
        exportresults = False
        globmessage = ("")
        def exportresults_change():
            global exportresults
            exportresults = not exportresults
        def flagchange():
            global flagchange
            global isfilemounted
            isfilemounted = not isfilemounted
        print ("Writing global arguments")
        flagchange()
        print ("Success")
        break
    except:
        print ("Error writing global arguments. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
        break
    ## MODULES ##
while True:
    try:
        print ("")
        print ("Attempting to write termination protocol")
        print ("    Attempting import sys.py")
        import sys
        print ("    System module successfully imported")
        def terminateapp():
            print ("")
            print ("Please report this to the developer. The application will now terminate.")
            input()
            sys.exit()
        print ("Success")
        break
    except ImportError:
        print ("Cannot open system module. Please ensure 'sys' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/sys.html")
        engine_error = 1
while True:
    try:
        print ("")
        print ("Attempting import linecache.py")
        import linecache
        print ("Linecache module successfully imported")
        break
    except ImportError:
        print ("Cannot open linecache module. Please ensure 'linecache' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/linecache.html")
        engine_error = 1
while True:
    try:
        print ("")
        print ("Wring clear-screen module")
        print ("    Attempting import os.py")
        import os
        print ("    OS module successfully imported")
        def clearscreen():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        print ("Success")
        print ("")
        print ("Writing library scan sub-module")

        def libraryscan():
            print("\nReturning files installed...")
            for textfile in os.listdir("./sys/lib"):
                if textfile.endswith(".txt"):
                    print(textfile)
                else:
                    print ("No supported files detected in /sys/lib.\nPlease ensure files entered are validated.\nSee 'About' for further support with this\n\nPress enter to return to the main menu.")
                    input()
                    ui()
        print ("Success")
        break
    except:
        print ("Cannot open os module or write clearscreen sub-module. Please ensure 'os' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/os.html")
        engine_error = 1
while True:
    try:
        print ("Attempting import re.py")
        import re
        print ("Regular expression module successfully imported") #Line 75
        break
    except ImportError:
        print ("Cannot open regular expression module. Please ensure 're' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/re.html")
        engine_error = 1
#########################
#START MOUNTING MODULE  #
#########################
while True:
    try:
        print ("Writing system mounting module")
        def sys_mount():
            while True:
                try:
                    global fail
                    global file
                    global player_ranks
                    clearscreen()
                    print ("Rustlemania Matchmaking Service: System Mount")
                    print ("*"*45)
                    libraryscan()
                    print ("\nPlease enter the filename you would like to mount including .txt extension.\nEntering no selection will return you to the previous menu.")
                    filename = input ("> ")
                    if filename == (""):
                        ui()
                    else:
                        filename = os.path.join("./sys/lib/", filename)
                        os_filename_tuple = (os.path.splitext(filename))
                        filename_extension = str(os_filename_tuple[1])
                        if filename_extension != (".txt"):
                            print ("\nPlease enter a .txt file")
                            sys_mount()
                        elif filename_extension == (".txt"):
                            regexp = re.compile (r"^(.*[|].*[|].*[|][1-9][0-9]*)$")
                            fail = False
                            playercount = 0
                            linepos = 0
                            file = open(filename, 'r')
                            for line in file.readlines():
                                result = regexp.search(line)
                                if result == None:
                                    if "##" in line:
                                        linepos += 1 #int linepos
                                        pass
                                    else:
                                        print(line)
                                        fail = True
                                        badplayer_position.append(linepos)
                                        linepos += 1
                                else:
                                    line = line.strip("\n") #Otherwise \n will show up in matchmaker
                                    split_line = line.split("|")
                                    player_usernames.append(split_line[0])
                                    player_steamurls.append(split_line[1])
                                    player_ranks.append(split_line[2])
                                    player_powerlevels.append(split_line[3])
                                    goodplayer_position.append(linepos)
                                    playercount += 1
                                    linepos += 1
                        if playercount == 0:
                            print("")
                            print("Error. No compatible players were detected in this fle.\nPlease ensure all of your data is formatted in the correct syntax.\nPressing enter will terminate the program.")
                            input()
                            sys.exit()
                        elif playercount >= 0:
                            ##########################
                            #Display results (table) #
                            ##########################
                            clearscreen()
                            print("Rustlemania Matchmaking Service: Results")
                            print("*"*40)
                            print ("\nFound...\n")
                            goodplayers = 0
                            badplayers = 0
                            print("\nVALID" + " " + "USERNAME" + " " + "STEAMURL" + " " + "RANK" + " " + "POWERLEVEL\n")
                            for i in range(len(goodplayer_position)):
                                print("VALID" + "  " + player_usernames[i] + "  " + player_steamurls[i] + "  " +player_ranks[i] + "  " +player_powerlevels[i])
                                goodplayers += 1
                            for i in range(len(badplayer_position)):
                                       print("VALID" + "  " + player_usernames[i] + "  " + player_steamurls[i] + "  " +player_ranks[i] + "  " +player_powerlevels[i])
                                       badplayers += 1
                            if fail is True:
                                print("Detected "+str(badplayers)+" invalid players in '"+os_filename_tuple[0]+"' (see data)")
                                print ("Please validate "+filename+" and try again.")
                                terminateapp()
                            while fail is False:
                                try:
                                    print("Detected "+str(goodplayers)+" players in '"+filename+"' (see data)")
                                    print ("\nIs this correct (Y/N)?")
                                    yes_no_input = input("> ")
                                    if yes_no_input == ("Y") or yes_no_input == ("y"):
                                        enumerate_rank_database()
                                    elif yes_no_input == ("N") or yes_no_input == ("n"):
                                        print("Please correct your data.")
                                        raise SystemExit
                                    else:
                                        print("Please enter a valid selection")
                                        continue
                                except ValueError:
                                    terminateapp()
                        else:
                                print ("")
                                print ("A critical error has occurred. Stop messing with my application.")
                                terminateapp()

                except IOError:
                    print("")
                    print("No such file")
                    input("Press enter to continue\n")
                    continue
                except ValueError:
                    print ("")
                    print ("Please enter a valid selection.")
                    continue
        print ("Success")
        break
    except:
        print ("Error writing sysmount. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1

#####################################################################################################################
#Enumerate rank database: create a set of tuples based on Ranks.txt.                                                                         #
# This way we can iterate over those tuples and set a powerlevel procedurally for each rank.                        #
# We will then append those ranks to rank_powerlevel database in the same order as Ranks.txt (strongest to weakest).#
#####################################################################################################################
while True:
    try:
        print ("Writing database management protocol")
        def enumerate_rank_database():
            #make the player_ranks great again
            ranksfile = open("./sys/cfg/Ranks.txt", 'r')
            regexp = re.compile (r"^(.*[|].*)$")
            no_playerranks = 0
            print()
            for line in ranksfile.readlines():
                if "##" in line:
                    pass
                else:
                    result = regexp.search(line)
                    if result:
                        line = line.strip('\n') #Remove trailing whitespace
                        split_line = line.split("|")
                        rank = (split_line[0], split_line[1])
                        rank_database.append(rank)
                        no_playerranks += 1   #The number of player ranks is used as a figure to determine the powerlevel for an independent player rank (/10000). We will later average this against the stated figure from each individual member.
                    elif not result:
                        print ("Please correct Ranks.txt")
                        terminateapp()
            rank_powerlevel_value = 10000 # Essentially the powerlevel per rank is calculated as a percentage of all ranks
            str_rank_powerlevel_value = str(rank_powerlevel_value)
            print("The most powerful player ranking has been set at a Powerlevel of "+str_rank_powerlevel_value+"!")
            for i in range(no_playerranks):
                powerlevel_database.append(int((rank_powerlevel_value/100)*(((no_playerranks-i)/no_playerranks)*100)))  #If, for example, Global is the first rank iterated over, then for powerlevel_database[0], the Global powerlevel will be calculated as 10000/1 = 10000. This means for Ranks.txt the strongest ranks should be placed at the beginning of the file.
            parse_ranks()
      ########################################################################################################################
      #Process ranks: assign ranks for each player based on ranks in rank_database (ranks.txt) and indicated player skill    #
      #For all players iterate over [0] and [1] of the tuple using rank.replace.                                             #
      # Since lists are mutable we don't need to create a new array (we can use the old one)                                 #
      ########################################################################################################################
        def parse_ranks():
            global player_powerlevels
            def process_ranks(player_ranks, rank_database):
                try:
                    rank_map = dict(rank_database)
                    return [rank_map[rank] for rank in player_ranks]
                except ValueError:
                    print("The ranks.txt file is invalid or inaccurate (sys/cfg).\nPlease correct this and try running the application again.")
                    terminateapp()
            def main_process_ranks():
                global processed_ranks
                print()
                print ("Ranks.txt is valid. Ranks will be mapped as follows...")
                print("Original player ranks:")
                print(player_ranks)
                processed_ranks = process_ranks(player_ranks, rank_database)
                print("Processed player ranks:")
                print(processed_ranks)
                return
            main_process_ranks()
            def undo_rank_database():
                global rank_database
                rank_database_parse = ([x[1] for x in rank_database]) #Returns Rank_database to first
                rank_database = rank_database_parse
                print()
                print("Finished!")
            undo_rank_database() # Turns rank_database from (Rank 1, Rank 1) to (Rank 1)
            print ()
            ######################################################################################################
            #Process_powerlevels(): now ranks are consistent and have a consistent value...                      #
            #Find the average of subjective player skill (input value) and ranked player skill (assigned value)  #
            ######################################################################################################
            print ("Calculating powerlevels for each player...\n")
            def process_powerlevels():
                global player_powerlevels

                for i in enumerate(processed_ranks):
                    for x in enumerate(rank_database):
                        if i[1] == x[1]:
                            input_rank_powerlevel = int(player_powerlevels[i[0]])
                            true_rank_powerlevel = int(powerlevel_database[x[0]])
                            parsed_powerlevel = (input_rank_powerlevel+true_rank_powerlevel)/2
                            calculated_powerlevels.append(parsed_powerlevel)
                            print("Player "+player_usernames[i[0]]+" gave rank "+i[1]+" and input powerlevel "+ str(input_rank_powerlevel)+" and recieved a calculated powerlevel "+str(parsed_powerlevel)+"!")
                            break
                        else:
                            continue
                print()
            process_powerlevels()
            player_powerlevels = calculated_powerlevels
            for i in range(len(player_powerlevels)):
                player_assignedteams.append(int(0))
            print("Finished!\n")
            print("The file "+filename+" has been successfully mounted. Please press any key to continue...")
            input()
            flagchange()
            ui()
        print ("Success")
        break
    except:
        print ("Error writing sys_mount module")
        engine_error = 1
###############################
#Sys_Unmount: clear all arrays#
###############################
while True:
    try:
        def sys_unmount():
            clearscreen()
            print ("Rustlemania Matchmaking Service: Unmount")
            print ("*"*45)
            print()
            global player_usernames
            global player_ranks
            global player_steamurls
            global processed_ranks
            global player_powerlevels
            global powerlevel_database
            global calculated_powerlevels
            global rank_database
            global badplayer_position
            global goodplayer_position
            global player_assignedteams
            global no_playerranks
            global  filename
            global no_playerranks
            global adjusted_player_powerlevels
            global matchmadeteams_processed
            global playerbase_configurationspace
            global matchmadeteams_configurationspace
            global teamsize
            global teamsbuilt
            player_usernames = []
            player_ranks = []
            player_steamurls = []
            processed_ranks = []
            player_powerlevels = []
            powerlevel_database = []
            calculated_powerlevels = []
            rank_database = []
            badplayer_position = []
            goodplayer_position = []
            player_assignedteams = []
            no_playerranks = 0
            filename = ("")
            no_playerranks = 0
            adjusted_player_powerlevels = []
            matchmadeteams_processed = [] #Not sure why this *populated array* displays as not used in my IDE ._.
            playerbase_configurationspace = []
            matchmadeteams_configurationspace = []
            teamsize = 0
            teamsbuilt = False
            flagchange()
            if isfilemounted == True:
                terminateapp()
            print ("Database successfully cleared.")
            ui()
        break
    except:
        print ("Error writing sys_unmount module")
        engine_error = 1
#########################
#  Teambuilder module   #
#########################
while True:
    try:
        print ("Writing matchmaking protocol")
        print ("    Attempting import math.py")
        import math
        print ("    Attempting import statistics.py")
        import statistics
        def sys_matchmaker():
            clearscreen()
            print ("Rustlemania Matchmaking Service: Team Builder")
            print ("*"*45)
            print ("\nPlease select team sizes you would like. No selection will return you to the main menu...")
            try:
                print ("\nThere are "+str((len(player_usernames)))+" participants.\n")
                teamsize = int(input("> "))
                if teamsize == (""):
                    ui()
                elif teamsize > len(player_usernames):
                    print("The size of teams cannot be greater than the number of participants. Please enter a smaller value")
                    input("Please press enter to continue...")
                    return
                elif teamsize < int(1):
                    print("\nYou must select at least two participants for a team (there's no I in team)!")
                    input("Please press enter to continue...")
                    return
            except ValueError:
                print("Please enter a value.")
                return
            clearscreen()
            print ("Rustlemania Matchmaking Service: Team Builder")
            print ("*"*45)
            print("\nBuilding sets of balanced teams equal to target average powerlevel. Please wait while working...")
            matchmade_powerlevels = []
            #We cant use the original powerlevels if we have to creep, since expanding the scope of the search means making changes to these values.
            matchmaking_powerlevels = player_powerlevels 
            matchmaking_powerlevels_sum = 0
            ################################################################################################################
            #Using subsets, create an average of all the powerlevels and then find every possible way to hit that average  #
            #We only output subsets equal to the selected teamsize                                                         #
            ################################################################################################################
            def subset_avg(numbers, target, partial=[]):
                    if len(partial) > 0:
                        s = math.ceil(sum(partial)/float(len(partial))) # calculate the average for each subset
                    else:
                        s = math.ceil(sum(partial)/float(1)) # calculate the average for first empty subset which is 0
                    # check if the partial sum is equals to target
                    if s == target:
                        if len(partial) == teamsize:
                            print ("Found possible team at powerlevels %s whose average equal to target =%s" % (partial, target))
                            matchmade_powerlevels.append(partial)
                    if s >= target:
                        return  # if we reach the number why bother to continue

                    for i in range(len(numbers)):
                        n = numbers[i]
                        remaining = numbers[i+1:]
                        subset_avg(remaining, target, partial + [n])
            ##################################################################################################################################
            #Increase scope.                                                                                                                 #
            # Using the new array, matchmaking_powerlevels, if we cannot find enough players we need to increase the scope of the search.    #
            # We achieve this by increasing the breadth of the independent player powerlevels by a given percentage.                         #
            # This avoids bugs when data is too close together                                                                               #
            ##################################################################################################################################
            scope_count = 0
            input_scope = 1
            while len(matchmade_powerlevels) < (2*teamsize) and matchmade_powerlevels == []: #We need at least two teams for a fair fight
                if input_scope == 100:
                    print("The input scope exceeded the algorithms matchmaking limitations. Please inform the developer and provide the list of players used for diagnosis.")
                    print("The application will now terminate")
                    terminateapp()
                matchmade_powerlevels = []
                for each_i in matchmaking_powerlevels:
                    matchmaking_powerlevels_sum += each_i # calculate the sum here
                    matchmaking_powerlevels_avg = math.ceil(matchmaking_powerlevels_sum/float(len(matchmaking_powerlevels))) # calculate the average here which becomes our target
                    subset_avg(matchmaking_powerlevels,matchmaking_powerlevels_avg)
                print ("Increasing matchmaking scope... "+str(scope_count)+" : "+str(input_scope))

                def increment_scope(input_list, scope):
                    searchlimiter = 2 #Make sure that we don't pick up many of the same larger values (imagine lots of 2's and 10's!)
                    mean = statistics.mean(input_list)
                    searchpositions = []
                    for x, i in enumerate(input_list):
                        if i == max(input_list) or i == min(input_list):
                            if searchlimiter != 0:
                                searchpositions.append(x)
                                searchlimiter -= 1
                    for i in searchpositions:
                        input_list[i] = (input_list[i] - mean) / scope + mean
                    return input_list
                increment_scope(matchmaking_powerlevels, input_scope)
                scope_count += 1
                input_scope += 1.0025
                print(matchmaking_powerlevels)
            ################################################################################################################################
            #Assign teams to player_assignedteams.                                                                                         #
            # Based on values stored in matchmaking_powerlevels (set of players) / matchmade_powerlevels (set of subset of possible) teams)#
            ################################################################################################################################
            player_assignedteams = []
            for i in range(len(matchmaking_powerlevels)):
                player_assignedteams.append(int(0))
            ##############################################################################################################################################################
            #Configuration space. Responsible for indicating whether...                                                                                                  #
            #  (a) a player from matchmaking_powerlevels has been assigned to a team or (b) a team has already been assigned to a player                                 #
            ##############################################################################################################################################################
            playerbase_configurationspace = []
            matchmadeteams_configurationspace = [] #detects if value in matchmade_powerlevels has been assigned (if going over a number which has been given value 1 but we need to give it value 2)

            for i in range(len(matchmaking_powerlevels)):
                playerbase_configurationspace.append(int(0))
            for x in matchmade_powerlevels:
                for y in x:
                    matchmadeteams_configurationspace.append(int(0))

            teamcount = len(matchmade_powerlevels[0])
            assignteam = 1 #Determines the base no. of teams to be assigned
            ##########################################################################
            #Flatten list of lists                                                   #
            #Because the endeavour of using for loops in subsets was getting insane  #
            ##########################################################################
            matchmadeteams_processed = []
            for x in matchmade_powerlevels:
                for y in x:
                    matchmadeteams_processed.append(y)
            print (matchmadeteams_processed)
            ####################################################################################################################################
            #Teammate handler: makes lookups into the configuration space to help determine whether either a player has been assigned to a team#
            ####################################################################################################################################
            def teammate_handler(isnotfreeplayer,isnotfreeslot, assignteam):
                if playerbase_configurationspace[isnotfreeplayer] == 0 and matchmadeteams_configurationspace[isnotfreeslot] == 0:
                    playerbase_configurationspace[isnotfreeplayer] = 1
                    matchmadeteams_configurationspace[isnotfreeslot] = 1
                    return int(1), assignteam #Outcome 1, safe to add player to empty slot, assign == value to be assigned
                #else either, player is set team, teammate of team is set team (or both):: do nothing
                elif playerbase_configurationspace[isnotfreeplayer] == 1 and matchmadeteams_configurationspace[isnotfreeslot] == 0:
                    return int(2) #Outcome 2, continue the for loop iterating through players since the player is not free but the slot is free
                elif playerbase_configurationspace[isnotfreeplayer] == 0 and matchmadeteams_configurationspace[isnotfreeslot] == 1:
                    return int(3) #Outcome 3, break the for loop iterating through slots and players since the slot is not free
                elif playerbase_configurationspace[isnotfreeplayer] == 1 and matchmadeteams_configurationspace[isnotfreeslot] == 1:
                    input()
                    return int(4)
                return int(5) #Unexpected error (catch all)
            ##############################################################################################################################
            #Matches players to each team and looks up to configuration space to see if either team-slot or player has been taken already#
            ##############################################################################################################################
            for teammatepos in enumerate(matchmadeteams_processed):
                if teamcount == 0:
                    assignteam += 1
                    teamcount = teamsize
                for playerpos in enumerate(matchmaking_powerlevels):
                    if playerpos[1] == teammatepos[1]:
                        if teammate_handler(playerpos[0], teammatepos[0], assignteam) == (1, assignteam):
                            player_assignedteams[playerpos[0]] = assignteam
                        else:
                            continue
                    else:
                        continue
                teamcount -= 1
            #Lots of cleanup to do (free up memory from arrays).
            matchmadeteams_processed = [] #Not sure why this *populated array* displays as not used in my IDE ._.
            playerbase_configurationspace = []
            matchmadeteams_configurationspace = []
            print ("\nCleaning up arrays...\n")
            matchmaking_powerlevels = [] # ._.
            print("Done!")
            global teamsbuilt
            teamsbuilt = True
            input("\nPlease press enter to continue")
            ui()
        print("Success")
        break
    except:
        print ("Error writing sys_matchmaker module. Please ensure the math and statistics modules in python are updated to the latest version.")
        engine_error = 1
#########################
#Search mounted database#
#########################
#SEARCH ENGINE
while True:
    try: #Line 235
        print ("Writing search-engine module")
        import time
        def sys_searchengine():
            while True:
                try:
                    clearscreen() 
                    print ("Rustlemania Matchmaking Service: Search Menu")
                    print ("*"*45)
                    print ("")
                    global teamsbuilt
                    global exportresults
                    usrinput = ""
                    op1 = player_usernames
                    if teamsbuilt != True:
                        print ("\nFor players not assigned to a team the value for their team will display as 0.\n")
                    def search_ui(op1, usrinput):
                        try:
                            print ("Please select one of the following options.")
                            print ("1. Search by username.")
                            print ("2. Search by in-game rank.")
                            print ("3. Search by team assigned.")
                            print ("4. Show all data.")
                            if exportresults:
                                print ("5. Set the application to not export search results data.")
                            else:
                                print ("5. Set search results to export.")
                            print ("6. Return to the UI.")
                            searchselection = int(input("> "))
                            if searchselection == 1 or 2 or 3 or 4 or 5: 
                                print()
                                if searchselection == 1:
                                    print ("Please enter the username.")
                                    op1 = player_usernames
                                elif searchselection == 2:
                                    print ("Please enter the in-game rank.")
                                    op1 = player_ranks
                                elif searchselection == 3:
                                    print ("Please enter the team number.")
                                    op1 = player_assignedteams
                                elif searchselection == 4:
                                    op1 = player_usernames
                                    return op1, usrinput
                                elif searchselection == 5:
                                    exportresults_change()
                                    sys_searchengine()
                                elif searchselection == 6:
                                    ui()
                                print ("\nEnter no data to return to the main menu.\n")
                                usrinput = input ('> ')
                                if usrinput == "":
                                    ui()
                                else:
                                    return op1, usrinput
                        except ValueError:
                            print ("Please enter a valid selection.")
                            search_ui(op1, usrinput)
                    op3 = search_ui(op1, usrinput)
                    op1 = op3[0]
                    op2 = op3[1]
                    def search_selection(selection):
                        clearscreen()
                        print ("Rustlemania Matchmaking Service: Results")
                        print ("*"*45)
                        print ("")
                        positionindex = []
                        position = 0
                        global  search_flag
                        search_flag = []
                        for op2 in op1:
                            if selection in op2:
                                    search_flag.append(1)
                                    positionindex.append(position)
                            position += 1
                        return positionindex
                    positionsfound = search_selection(op2)
                    if search_flag != []:
                        date_time = time.strftime("%d.%m.%Y-%H%M%S")
                        try:
                            if exportresults:
                                f = open("Search Results " + str(date_time) + " .txt", 'w')
                                f.write("USERNAME"+"    "+"RANK"+"    "+"POWERLEVEL"+"    "+"ASSIGNED TEAM\n")
                        except IOError:
                            print("Could not export results to file.\nPlease ensure that you have read and write access to the local directory this application is contained in.")
                            print("\n The application will now terminate.")
                            terminateapp()
                        print ("USERNAME"+"    "+"RANK"+"    "+"POWERLEVEL"+"    "+"ASSIGNED TEAM\n")
                        while positionsfound != []:
                            i = positionsfound.pop(0)
                            print (str(player_usernames[i])+" "+str(player_ranks[i])+" "+str(player_powerlevels[i])+" "+str(player_assignedteams[i]))
                            if exportresults:
                                try:
                                    f.write(str("\n"+player_usernames[i])+" "+str(player_ranks[i])+" "+str(player_powerlevels[i])+" "+str(player_assignedteams[i]))
                                except IOError:
                                    print("Could not export results to file.\nPlease ensure that you have read and write access to the local directory this application is contained in.")
                                    print("\n The application will now terminate.")
                                    terminateapp()
                            if positionsfound == []:
                                if exportresults:
                                    try:
                                        f.close()
                                        print("\nResults have been successfully exported as 'Search Results " +str(date_time)+".txt' in the application's local directory\n")
                                    except IOError:
                                        print(" A critical error has occurred: could not end exportation process. \nPlease ensure that you have read and write access to the local directory this application is contained in.")
                                        terminateapp()
                                break
                    else:
                        print ("There are no records which match your search.")
                        print ("Press enter to return to search options.")
                        input ()
                        sys_searchengine()
                    print ("")
                    input("Press enter to return to the main menu.")
                    ui()
                except ValueError:
                    print ("")
                    print ("Please make a valid selection")
                    print ("Press enter to return to the search options screen")
                    input ()
                    sys_searchengine()
        print ("Success")
        break
    except:
        print ("Error writing search_engine protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed, the time module is present, and that you are running a version of Python 3 or higher.")
        engine_error = 1
################
#Readme Module #
################
while True:
    try:
        print("Writing assistance")
        import textwrap
        def sys_about():
            clearscreen()
            print ("Rustlemania Matchmaking Service: About")
            print ("*"*45)
            print ()
            try:
                about = open("./sys/static/readme.txt", "r")
                lines = about.readlines()
                for i in lines:
                    print(textwrap.fill(i, width=80))
                about.close()
                print("\nPlease press enter to return to the main menu.")
                input()
            except IOError:
                print("Readme file not found in 'sys\static' directory.")
                print("Please press enter to return to the main menu\n")
                input()
                ui()
        print("Success")
        break
    except:
        print ("Error writing UI or pathways (sys_about). Please ensure the textwrap module is installed. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
################################
#Doom-inspired Quit: detects OS#
################################
while True:
    try:
        print("Writing jokes...")
        def sys_exit():
            if os.name == "nt":
                print ("\nYou're trying to say you like Windows better than me, right?")
            else:
                print ("\nAre you sure you want to go proc yourself?")
            confirm = input("> ")
            if confirm == ("y"): #or statement failure
                sys.exit()
            elif confirm == ("Y"):
                sys.exit()
            elif confirm == ("yes"):
                sys.exit()
            elif confirm == ("Yes"):
                sys.exit()
            else:
                ui()
        print ("Success")
        break
    except:
        print ("Error writing UI or pathways (sys_exit). Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
###############
#UI Module    #
###############
while True:
    try:
        print ("Writing UI")
        def ui():
            while True:
                try:
                    global filename
                    clearscreen()
                    print ("Rustlemania Matchmaking Service: Main Menu")
                    print ("*"*45)
                    print (globmessage)
                    print ("\nWelcome to the main menu\n")
                    print ("Please select from one of the following options:")
                    if isfilemounted == False:
                        print ("1. Mount a database of players to be matchmade")
                        print ("2. About")
                        print ("3. Quit")
                    else:
                        print ("1. Un-mount "+filename)
                        print ("2. Matchmake the players (will scramble existing teams)")
                        print ("3. Perform a search through the mounted database")
                        print("4. About")
                        print ("5. Quit")
                    menuinput = int(input("> "))
                    if menuinput == (1) and isfilemounted == False:
                        sys_mount()
                    elif menuinput == (2) and isfilemounted == False:
                        sys_about()
                    elif menuinput == (3) and isfilemounted == False:
                        sys_exit()
                    elif menuinput == (1) and isfilemounted == True:
                        sys_unmount()
                    elif menuinput == (2) and isfilemounted == True:
                        sys_matchmaker()
                    elif menuinput == (3) and isfilemounted == True:
                        sys_searchengine()
                    elif menuinput == (4) and isfilemounted == True:
                        sys_about()
                    elif menuinput == (5) and isfilemounted == True:
                        sys_exit()
                except ValueError:
                    print ("")
                    print ("Please enter a valid selection.")
                    print ("Pressing enter will return you to the main menu.")
                    input ()
                    ui()
        print ("Success")
        break
    except:
        print ("Error writing UI or pathways. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
######################
#END USER INTERFACE  #
######################
if engine_error == 1:
    print ()
    print ("An error has occurred. Please see log above for details. Press any key to terminate the application.")
    input ()
else:
    ui()
