######################################################################################################################################################################################

#README:

#1. This program pre-defines all the necessary parts for the index service before they are executed within that program (the index service).
 #1a. Those necessary-parts or 'sub-modules' are passively introduced by the function "def" (definiton).
 #1a. The actual parameters or arguments of the predefined code are via this means not then executed until the relevant function is called.

   #1a. For example the parameters of an argument:
   #def():
   # print ("This is an example")
   #This predetermines an argument to print the text "This is an example". That argument can be executed by calling the function def().
   #If 'def()' as above were a necessary condition for the program to execute, then 'def()' would be issued as a sub-module (or part of a sub-module).
 #1b. The method of calling functions allows the user to interactively jump between the component features of the code.
  #1b. This allowing the programmer room to construct various ways in which the program interacts with the user, i.e. calling functions in a way which builds menus and user-interfaces.
  #1b. For instance this allows the programmer to pre-define the sub-modules which the program requires in while loops.
   #1b. Defining each sub-module in while loops allows the programmer to define exceptions (error-messages) in the event that the program fails to predefine any such function. 
 #1c. The user-interface or main menu is herein executed after all the aforementioned component parts are predefined sucessfully (by calling 'ui()').

#2. These comments will break down the predefinitions for each function for each relevant sub-module.
 #2a. However given that the the defining of and the sub-modules both take place in a while loop the following will occur:
  #2a. The explanatory process regarding the pre-definition of each sub-module (before the programs execution) will be explained in the comments before each relevant while loop
  #2a. The arguments of the functions themselves, taking place assuming the programs successful execution, will be explained within the nested function.
   #2a. For instance consider the following:
    #Line 1.   while True:
    #Line 2.       try:
    #Line 3.           def example():
    #Line 4.               print ("Example")
    #Line 5.               example()
    #Line 6.       except:
    #Line 7.            ("Error defining the example module")
   # Comments will be issued as follows:
    #
    #
    # [#### What the block does or discourse of the block of programming ####]
    
    # [COMMENTS FOR LINES 1/2 and LINES 6/7 (concerned with initializing the program):]
    #spacing#
 #  # [COMMENTS FOR LINES 3/4/5 (concerned with the execution within the program itself):]


    #   while True:
    #       try:
    #spacing#
    #           def example():
    #               print ("Example")
    #               example()

    #       except:
    #           ("Error defining the example module")
    #[Repeat]
######################################################################################################################################################################################

# The Erinaceous Flux Index Service. Version 1.0.
# This program was designed by:
# Callum Dempsey Leach. 200715849. COMP 1036. May 2013.
# Property of Callum Dempsey Leach and Leeds University.
# For Python 3(+) only.

    
#Lines 1/2/3/4/5: Introduces the program and informs the user that the program is initializing the engine. The engine, in other words, referring to what the program necessitates for operation (the sub-modules).
print ("Erinaceous-flux Index Service") #Line 1 begins here.
print ("*"*35)
print ("")
print ("")
print ("Initializing engine.") #Line 5

####Write global parameters: sets mostly but not limited to global variables required for the program to initialize or function.####

#Line 6/7: while True, try to write the following.
#Line 8: Informs the user that the application is writing (neccessary) global parameters. The following will be used later in the program.
        # They are defined now since this ensures that their definition will be successful before the program starts; so no issues when the program has initialized).
#Line 9: Creates the list "authors"
#Line 10: Creates the list "year"
#Line 11: Creates the list "title"
#Line 12: Creates the list "journal"
#Line 13: Sets engine error to 0. Engine error is an error-check the program does before initialization. If Engine Error = 1, the program will not initialize.
#Line 14: Sets flag to True. Flag will be used later in the program and denotes whether or not the program has a file or database mounted into the service.
        # If the flag is set to True then this indicates that there is a file mounted into the program.
        # If the flag is set to False then this indicates that there is not a file mounted into the program.
#Line 15: Sets globmessage to "". Globmessage is used to indicate the user not only that there is a file mounted into the system but also which file is mounted into the system (shown within the main menu) 
#Line 16/17/18/19: Creates a new function known as "flagchange". Flagchange toggles the flag between truth and falsity, by issuing that the flag now is equal to "not" the flag. 
                 # Note that in order to change the value of any global variable (i.e. "flag") within Python that variable must be previously restated as a global variable within the same function. 
#Line 21/22/23/24: Sets sets the following lists as global variables: authors; file; journal; and globmessage.
#Line 25/26: Calls the two defined functions so that the contents of those functions are interpreted.
#Line 27/28/29: Informs the user that the global arguments were written successfully.
#Line 30/31/32/33: The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to set any relevant global variable.
                 # engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.
while True: #Line 6
    try: #Line 7
        print ("Writing global arguments") #Line 8
        authors = []
        year = [] #Line 10
        title = []
        journal = []
        engine_error = 0
        flag = True
        globmessage = ("") #Line 15
        def flagchange():
            global flagchange
            global flag
            flag = not flag
        def setglobalvar(): #Line 20
            global authors
            global file
            global journal
            global globmessage
        setglobalvar() #Line 25
        flagchange()
        print ("Success")
        print ("")
        break
    except: #Line 30
        print ("Error writing global arguments. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
        break #Line 33

#####Import the necessary modules required for the program to initialize or function.####
     ##Also creates the clearscreen() sub-module as the "os" module is initialized.##

####SYS MODULE####

#Line 34/35: while True, try to write the following.
#Line 36/37/38/39/40: Informs the user that the system is attempting to import the module sys.py; and notifies the user if successful.
#Line 41/42  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to import that module
 #Line 43: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.
while True: #Line 34
    try: #Line 35
        print ("")
        print ("Attempting import sys.py")
        import sys
        print ("System module successfully imported")
        break #Line 40
    except ImportError:
        print ("Cannot open system module. Please ensure 'sys' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/sys.html")
        engine_error = 1 #Line 43

####LINECACHE MODULE####

#Line 44/45: while True, try to write the following.
#Line 46/47/48/49/50: Informs the user that the system is attempting to import the module linecache.py; and notifies the user if successful.
#Line 51/52  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to import that module
 #Line 53: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.
while True: #Line 44
    try: #Line 45
        print ("")
        print ("Attempting import linecache.py")
        import linecache
        print ("Linecache module successfully imported")
        break #Line 50
    except ImportError:
        print ("Cannot open linecache module. Please ensure 'linecache' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/linecache.html")
        engine_error = 1 #Line 53

####OS MODULE####
  ##CLEARSCREEN SUB-MODULE##

#Line 54/55: while True, try to write the following.
#Line 56/57/58/59/60/67: Informs the user that the system is attempting to import the module os.py; and notifies the user if successful.
#Line 68/69  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to import that module
 #Line 70: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.
#Line 68/69  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to import that module or write the clearscreen sub-module related.
#Line 70: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.

####CLEAR SCREEN SUB MODULE: clears the interpreter window####
#Line 62: Define the sub-module "clearscreen" called by inputting 'clearscreen()'.
 #Line 63/64/65/66. These lines are of the clearscreen sub-module. If the operating system is Windows (nt) then Python calls os.system('cls') which is the command for clear screen used by Windows system interpreters. For other operating systems os.systems ('clear') as an attempt to negate compatibility issues.
while True: #Line 54
    try: #Line 55
        print ("")
        print ("Attempting import os.py")
        import os
        print ("OS module successfully imported") #Line 60
        print ("Writing clear-screen sub-module") #Line 61

        def clearscreen(): #Line 62
            if os.name == 'nt':
                os.system('cls')
            else: #Line 65
                os.system('clear')
        break #Line 67
    except:
        print ("Cannot open os module or write clearscreen sub-module. Please ensure 'os' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/os.html")
        engine_error = 1 #Line 70

#### RE MODULE ####

#Line 71/72: while True, try to write the following.
#Line 73/74/75/76: Informs the user that the system is attempting to import the module re.py; and notifies the user if successful.
#Line 77/78  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to import that module
#Line 79: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.
while True: #Line 71
    try:
        print ("Attempting import re.py")
        import re
        print ("Regular expression module successfully imported") #Line 75
        break
    except ImportError:
        print ("Cannot open regular expression module. Please ensure 're' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/re.html")
        engine_error = 1

#####VALIDATION AND PARSE SUB-MODULE: Allows a user to mount a file. Then checks a file-mounted for goodness. Then loads information into arrays by author/year .etc. ready for use by the parsing module ####

#Line 80/81: while True, try to write the following.
#Line 82/83/155/156: Informs the user that the system is attempting to write the sub-module; and notifies the user if successful.
#Line 155/156/157:  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to write that sub-module. Otherwise, given there are no errors, the user is notified that the validation and parse sub module was written successfully.
#Line 160: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.

#Line 86: Define the function valiparse as what follows (so that when valiparse() is called the following occurs).
#Line 85/86: while True, try to write the following.
#Line 144 - 154: The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to mount the file given in the user input (filename), returning a prompt to enter a valid filename; then valiparse() is called to return the user to the beginning of the Mount Menu (where the user selects what file to mount).
#Line 87/88/89/90: Execute the clearscreen function: clears the window, then informs the user the whereabouts they are in the program by displaying a clear header.
#Line 91/92/93/94/95/96: Prompt the user to enter a filename (or none for further options) followed by a file extension to be mounted.
 #Line 97-107: If no file-name is entered then clear the screen and present an Additional Options menu: asking for an additional input to perform other functions.
    #Line 108/109: If that user input is equal to one, then call valiparse(), returning the user back to the mount menu.
    #Line 110/111: Otherwise if that user input is equal to two, then call ui(), returning the user back to the main menu.
    #Line 112/113/114/115/116/117: If it is not the case that the user selection equals one or two or if it is the case that that selection is equal to a number smaller than one or greater than 2 i.e. -1 and, then prompt the user to make a valid selection and return him to the mount menu (by calling valiparse()).
#Line 118: Compiles the regular expression pattern "^(.*\t(?!\s).*\t(?!\s).*\t(?!\s).*)$" into a regular expression object named "regexp".

 #Regular expression argument "regexp:
  #Line 118: 1. Regular expression objects match patterns character by character. However the dollar sign and carat are understood to compliment each other, matching the beginning and end of the characters in the string.
  #Line 118: 2. "." indicates any character; and * can be used to match any character in a string over an infinite number of iterations. So .* can semantically substitute the string "480238432u032ur80fh0f0vh0h0fhewfh08" .etc.
  #Line 118: 3. However the regular expression contains .*\t. \t represents a 'tab' number of whitespaces This means then, any characters (under an infinite number of iterations) followed by a tab. Therefore that regex (regular expression) could semantically substitute the string "Hello my name is callum   " (where the whitespace is a tab), but not "Hello my name is callum" (without a tab).
  #Line 118: 4. But given it is sufficient to represent any character to also represent a white-space the regex .*\t.*\t could also incorporate spaces in and between the tab characters i.e. the regex could semantically substitute the string "Hello my name is Callum[tab][space]And"
  #Line 118: 5. The specification explicitly states that the information in the file or database mounted can be valid iff (if and only if) the fields Author Year Title and Journal are separate by tab.
  #Line 118: 6. Therefore it is not acceptable to allow additional white-spaces in between the separation and each field; so the formula "3." would be invalid.
  #Line 118: 7. The formula "x(?!y)" matches the regular expression "x" iff that regular expression is not followed by regular expression "y".
  #Line 118: 8. Where \s is equal to a single whitespace; then integrated into the regular expression ".*\t(?!\s)" reads as 'all characters followed by a tab whitespace iff those characters are not followed by a single whitespace'.
  #Line 118: 9. Therefore .*\t(?!\s) is valid. The formula succeeds.

#Line 119/120: Sets "file" to global, and opens the file to read as "file" given by the user input ("filename").
#Line 121/122: For each line within the file, read those lines and match them against the regular expression object "regexp". If it is sufficient to have "regexp" to create that line (for each line) then this returns a MatchObject, otherwise it returns None.
 #Line 123/124/125: If the term "None" is returned then set the variable 'read' to 0 and break (stop reading the file) - goes to Line 133.
 #Line 126-132: Otherwise hold the value "read" as 1. For that line (where read is equal to 1), for each field (posited as tab separated), append the information of each field to the following arrays (lists) Authors (from first field, authors []) Year (from second field, year []) Title (from third field, title []) and Journal (fourth field, journal []).

#Lines 133-144: "read" was held as a flag to indicate if there are any bad lines in the file. If there is a bad line then the program, then, prompts the user and terminates. Otherwise the program continues by loading the parsing sub-module by calling the function parser()
while True: #Line 80
    try:
        print ("")
        print ("Developing valiparse sub-module")

        def valiparse():
            while True: #Line 85
                try:
                    clearscreen()
                    print ("Erinaceous-flux Index Service: Mount Menu")
                    print ("*"*35)
                    print () #Line 90
                    print ("Enter a filename followed by its file extension to mount.")
                    print ("The file will be located in the program directory if no directory is supplied.")
                    print ("Enter no input for additional options.")
                    print ("")
                    global filename #Line 95
                    filename = input ("> ")
                    if filename == (""):
                        clearscreen()
                        print ("")
                        print ("Erinaceous-flux Index Service: Mount Menu") #Line 100
                        print ("*"*35)
                        print ()
                        print ("Additional options")
                        print ("")
                        print ("1. Return to previous menu.") #Line 105
                        print ("2. Quit mount.")
                        additional_selection = int(input("> "))
                        if additional_selection == 1:
                            valiparse()
                        elif additional_selection == 2: #Line 110
                            ui()
                        elif additional_selection != 1 or 2 or additional_selection > 1 or additional_selection < 2:
                            print ("")
                            print ("Please make a valid selection on the screen")
                            print ("Press enter to return to the mount menu.") #Line 115
                            input ()
                            valiparse()
                    regexp = re.compile (r"^(.*\t(?!\s).*\t(?!\s).*\t(?!\s).*)$")
                    global file
                    file = open (filename, 'r') #Line 120
                    for line in file.readlines():
                        result = regexp.search(line)
                        if result == None:
                            read = 0
                            break #Line 125
                        else:
                            read = 1
                            split_line = line.split ("\t")
                            authors.append(split_line [0])
                            year.append(split_line[1]) #Line 130
                            title.append(split_line[2])
                            journal.append(split_line[3])
                    if read == 0:
                        print ("")
                        print ("Error. This file or its formatting inclusively is incompatible with this system.") #Line 135
                        print ("")
                        print ("Please ensure all of your data is formatted in the correct syntax (see about for details)")
                        print ("")
                        print ("Pressing enter will terminate the program.")
                        input () #Line 140
                        sys.exit()
                    elif read == 1: #FILE GOOD. PARSE
                        parser()
                except IOError:
                    clearscreen() #Line 145
                    print ("Erinaceous-flux Index Service: Warning")
                    print ("*"*35)
                    print ("")
                    print ("Error. The file you entered does not exist.")
                    print ("") #Line 150
                    print ("Please enter a different file name.")
                    print ("Press enter to continue.")
                    input ("") #Line 154

        print ("Success") #Line 155
        break
    except:
        print ("Error writing 'validation and parsing' protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        print ("If you are still encountering this error proceeding that action it is possible the 're' module found within the default installation package no longer supports any of the commands issued in this program or they have been tampered with.")
        engine_error = 1 #Line 160

#####PARSING SUB-MODULE: Parses a valid file so it is ready for use by the search engine ####

#Line 161/162: while True, try to write the following.
#Line 163/201/202: Informs the user that the system is attempting to write the sub-module; and notifies the user if successful.
#Line 203/204/205:  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to write that sub-module. Otherwise, given there are no errors, the user is notified that the validation and parse sub module was written successfully.
#Line 206: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.

#Line 164: Define the function parser as what follows (so that when parser() is called the following occurs).
#Line 165/166/167/168/169: Sets authors, year, title, journal to global variables. It is required for a global variable, as in this instance, to be called once predefined in order for it to be modified.

#Line 170: Creates a new list named parsed authors.
#Line 170 - 175: These lines use a Modus-Ponens (if A then B. A. Therefore B. If B then C. B. Therefore C. [.etc.]) style of argument to translate the authors into an acceptable format.
 #Line 171: Allow the call parse_author for every line in authors array.
    #Line 172: For parse_authors (which starts with the first iteration), substitute all items in the string which are the regular expression "semi-colon" into colons. I.e. "Jack;Sparrow" becomes "Jack,Sparrow" Name that substitution parsed_authors_a
    #Line 173: For that line (parsed_authors_a) add a full-stop proceeding the final character of the string by reading the whole string and substiting all the characters with a version of the same string with a full stop on the end. I.e. "Jack, Sparrow" becomes "Jack, Sparrow". Name that substitutiton parsed_authors_b
    #Line 174: For that line (parsed_authors_b) substitute "," with " & " iff "," is not followed by a whitespace a word and a full-stop. I.e. given "Jack,Sparrow" becomes "Jack & Sparrow". Name that substitution parsed_authors_c.
    #Line 175: Given the string parsed_authors_c append this to the list "parsed authors".
#Line 176/177: Once complete (all lines have been processed,   array authors = parsed_authors, clear the array parsed_authors (applied as a resolution during de-bugging).

#Line 178: Creates a new list named parsed_years.
#Line 179: Allow the call parse_year for every line in years array.
 #Line 180: Substitute every entire string of every four numbers (any number denoted by \d) with the same string with the addition of a full stop and brackets. I.e. 1/1/1/1 becomes (1/1/1/1) whereby YEAR does not become (YEAR). Name that string parsed_year.
#Line 181: For every item parsed_year add it to the array parsed_years.
#Line 182/183: Once complete (all lines have been processed), array year = parsed_years (applied as a resolution during de-bugging), clear the array parsed_years.

#Line 184: Creates a new list named parsed_titles
#Lien 185: Allow the call parse_title for every line in titles array.
 #Line 180: Substitute every entire string of any set of characters with the same string with the addition of a full stop. I.e. Jack becomes Jack. Name that string parsed_title.
#Line 181: For every item parsed_title add it to the array parsed_titles.
#Line 182/183: Once complete (all lines have been processed), array title = parsed_titles (applied as a resolution during de-bugging), clear the array parsed_titles.

#Line 190: Creates a new list named parsed_journals
#Lien 191: Allow the call parse_journal for every line in journals array.
 #Line 192: Substitute every entire string of any set of characters with the same string with the addition of a full stop before the final character (applied as a resolution during debugging: line-breaks "/b" at end of string in .txt file). I.e. Jack becomes Jack. Name that string parsed_title.
#Line 193: For every item parsed_journal add it to the array parsed_journals.
#Line 194/195: Once complete (all lines have been processed), array journal = parsed_journals (applied as a resolution during de-bugging), clear the array parsed_journals.
#Line 196-203: Inform the user that the file has been mounted successfully. Then set the global variable "globmessage" to inform the user which file is mounted (to be displayed in the main menu). Toggles the flag so that the flag indicating that a file has been mounted within the system. Returns to main menu.
while True: #Line 161
    try:
        print ("Developing parsing sub-module")

        def parser():
                global authors #Line 165
                global year
                global title
                global journal
                print
                #PARSE AUTHORS
                parsed_authors = [] #Line 170
                for parse_author in authors:
                    parsed_author_a = re.sub (r"[;]", ", ", parse_author)
                    parsed_author_b = re.sub (r"(.*)" , (parsed_author_a+"."), parsed_author_a)
                    parsed_author_c = re.sub (r",(?=\s[\w]+[.])", " & ", parsed_author_b)
                    parsed_authors.append(parsed_author_c) #Line 175
                authors = parsed_authors
                parsed_authors = []
                #PARSE YEARS
                parsed_years = []
                for parse_year in year:
                    parsed_year = re.sub(r"^(\d\d\d\d)$", ("("+parse_year+")"+"."), parse_year) #Line 180
                    parsed_years.append(parsed_year)
                year = parsed_years
                parsed_years = []
                #PARSE TITLE
                parsed_titles = []
                for parse_title in title: #Line 185
                    parsed_title = re.sub (r"(.*)" , (parse_title+"."), parse_title)
                    parsed_titles.append(parsed_title)
                title = parsed_titles
                parsed_titles = []
                #Parse Journals
                parsed_journal = [] #Line 190
                for parse_journal in journal:
                    parsed_journals = re.sub (r"^(.*)$" , (parse_journal[:-1]+"."), parse_journal)
                    parsed_journal.append(parsed_journals)
                journal = parsed_journal
                parsed_journal = [] #Line 195
                global  globmessage
                print ("File mounted successfully")
                print ("") 
                globmessage = (filename+" is the current file mounted.")
                print ("Please press enter to return to the main menu.") #Line 200
                input ()
                flagchange()
                ui() #Line 203
        print ("Success")
        break
    except:
        print ("Error writing parsing protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        print ("If you are still encountering this error proceeding that action it is possible the 're' module found within the default installation package no longer supports any of the commands issued in this program or they have been tampered with.") #Line 205
        engine_error = 1 #Line 206

#####UNMOUNTER SUB-MODULE: Unmounts a currently mounted file.####

#Line 207/208: while True, try to write the following.
#Line 209/235: Informs the user that the system is attempting to write the sub-module; and notifies the user if successful.
#Line 237/238:  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to write that sub-module. Otherwise, given there are no errors, the user is notified that the validation and parse sub module was written successfully.
 #Line 239: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.

#Line 210: Defines the unmount sub-module so it can be called with unmount()
#Line 211 - 234: Clears all the arrays and sets the filename to "". Toggles the flag so the program recognises there is no file mounted.



while True: #Line 207
    try:
        print ("Developing un-mounter sub-module")
        def unmount(): #Line 210
            clearscreen()
            print ("Erinaceous-flux Index Service: Un-mount")
            print ("*"*35)
            print ("")
            print ("Un-mounting current database: clearing arrays:") #Line 215
            print ("")
            global authors
            global year
            global title
            global journal #Line 220
            global globmessage
            global filename
            authors = []
            year = []
            title = [] #Line 225
            journal = []
            flagchange()
            file.close()
            globmessage = ("")
            print (filename+" has been successfully dismounted") #Line 230
            filename = ""
            print ("")
            print ("Press enter to return to the main menu.")
            ui()
        print ("Success") #Line 235
        break
    except:
        print ("Error writing un-mount protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1

#####SEARCH-ENGINE SUB-MODULE: Searches through a currently mounted file.####

#Line 234/235: while True, try to write the following.
#Line 209/235: Informs the user that the system is attempting to write the sub-module; and notifies the user if successful.
#Line 342/341:  The while True function is exploited to allow for an error message. That error message will inform the user that Python has failed to write that sub-module. Otherwise, given there are no errors, the user is notified that the validation and parse sub module was written successfully.
 #Line 343: engine_error is set to 1 informing the program that there has been an issue or error initializing any member of the engine.

#Line 240- 305: Clears screen and publishes header for user. Independently assigns the journal or author as the term "op 2" to denote Operation 2, which alternates between being the journal or author array. This is since "Op1" on the other hand is always equal to the user input. That way allowed me to shorten the search engines code later on (not having to define independent parameters for searching either authors and journals). Additional search option menus are posited.
#Line 306-310: Defines position index array, pointer position, and search flag.
#Line 311-315: For every operation 1 (user input) in operation 2 (array specified). If the search selection (user input) is in the array operation 2. Add "1" to the search flag (there has been a hit). Append the position of that hit to the position index array. Move pointer position down by one. Repeat for every line.
#Line 316-323: All "positions found" are equal to the positions in generated from the search. If the search flag is not empty (there was a hit) then for every position found in the index take that position and call it i (pop takes the position and denotes it, akin to cut and paste). Print out the author, year, title, and journal at those positions and delete that position from the index. When all the records are deleted (the index of positions = []), stop.
#Line 324-339: If no positions found inform the user that there were no hits in the search engine. Uses linecache.clearcache to clear all the temporary arrays. Returns to user interface. Expects value errors in-case user enters none-integer inputs.


#SEARCH ENGINE
while True:
    try: #Line 235
        print ("Developing search-engine sub-module")
        def search_engine():
            while True:
                try:
                    clearscreen() #Line 240
                    print ("Erinaceous-flux Index Service: Search Menu")
                    print ("*"*35)
                    print ("")
                    print ("Would you like to search by author or journal?")
                    print ("1. Author") #Line 245
                    print ("2. Journal")
                    print ("")
                    def additional_search_options():
                        clearscreen()
                        print ("Erinaceous-flux Index Service: Search Menu") #Line 250
                        print ("*"*35)
                        print ("")
                        print ("Additional options")
                        print ("")
                        print ("1. Show all data. This may take a couple minutes.") #Line 255
                        print ("2. Return to previous menu.")
                        print ("3. Quit search")
                        print ("")
                        additional_selection = int(input("> "))
                        if additional_selection == 1: #Line 260
                            pass
                        elif additional_selection == 2:
                            clearscreen()
                            search_engine()
                        elif additional_selection == 3: #Line 265
                            ui()
                        elif additional_selection != 1 or 2 or additional_selection > 1 or additional_selection < 2:
                            print ("")
                            print ("Please make a valid selection")
                            print ("Press enter to return to the search options screen") #Line 270
                            input ()
                            search_engine()
                    searchselection = int(input("> "))
                    if searchselection == 1: #Line 275
                        clearscreen()
                        print ("Erinaceous-flux Index Service: Search Menu")
                        print ("*"*35)
                        print ("")
                        print ("Enter the author you would like to search.") #Line 280
                        print ("Enter no input for additional options.")
                        print ("")
                        op1 = authors
                        op2 = input ('> ')
                        op3 = journal #Line 285
                        if op2 == (""):
                            additional_search_options()
                    elif searchselection == 2:
                        clearscreen()
                        print ("Erinaceous-flux Index Service: Search Menu") #Line 290
                        print ("*"*35)
                        print ("")
                        print ("Enter the journal you would like to search.")
                        print ("Enter no input for additional options.")
                        print ("") #Line 295
                        op1 = journal
                        op2 = input ('> ')
                        if op2 == (""):
                            additional_search_options()
                    elif searchselection != 1 or 2 or searchselection > 1 or searchselection < 2: #Line 300
                        print ("")
                        print ("Please make a valid selection")
                        print ("Press enter to return to the search options screen")
                        input ()
                        search_engine() #Line 305
                    def search_selection(selection):
                        positionindex = []
                        position = 0
                        global  search_flag
                        search_flag = [] #Line 310
                        for op2 in op1:
                            if selection in op2:
                                    search_flag.append(1)
                                    positionindex.append(position)
                            position += 1 #Line 315
                        return positionindex
                    positionsfound = search_selection(op2)
                    if search_flag != []:
                        while positionsfound != []:
                            i = positionsfound.pop(0) #Line 320
                            print (authors[i]+" "+year[i]+" "+title[i]+" "+journal[i])
                            if positionsfound == []:
                                break
                    else:
                        print ("There are no records which match your search.") #Line 325
                        print ("Press enter to return to search options.")
                        input ()
                        search_engine()
                    print ("")
                    input("Press enter to return to the main menu.") #Line 330
                    linecache.clearcache()
                    ui()
                except ValueError:
                    print ("")
                    print ("Please make a valid selection") #Line 335
                    print ("Press enter to return to the search options screen")
                    input ()
                    search_engine()
        print ("Success")
        break #Line 340
    except:
        print ("Error writing search_engine protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1 #Line 343

####USER INTERFACE MENU####
#Lines 344 onwards. Navigates through various menus based on the circumstances provided

#User Interface
while True: #Line 344
    try:
        print ("Writing user-interface sub-module")
        def ui():
            while True:
                try:
                    clearscreen()
                    print ("Erinaceous-flux Index Service: Main Menu")
                    print ("*"*35)
                    menuinput = 0
                    menuinput2 = 0
                    print ("")
                    print ("Welcome to the main menu.")
                    print ("")
                    print ("Please select from among the following options:")
                    print ("1. Mount a file or database.")
                    print ("2. Search a mounted file or database by author or journal (or conference).")
                    print ("3. About/Disclaimer.")
                    print ("4. Quit the program")
                    if globmessage == "":
                        menuinput = int(input("> "))
                    else:
                        print ("")
                        print (globmessage)
                        print ("")
                        menuinput = int(input("> "))
                    if menuinput == (1):
                        clearscreen()
                        print ("Erinaceous-flux Index Service Database Options ")
                        print ("*"*40)
                        print ("")
                        print ("Welcome to the database options menu.")
                        print ("")
                        print ("Please select from among the following options:")
                        print ("1. Mount a database.")
                        print ("2. Un-mount an existing database.")
                        print ("3. Return to the main menu.")
                        if globmessage == "":
                            menuinput2 = int(input("> "))
                        else:
                            print ("")
                            print (globmessage)
                            print ("")
                            menuinput2 = int(input("> "))
                        if menuinput2 == ((1) and flag == False):
                            valiparse()
                        elif menuinput2 == ((1) and flag == True):
                            clearscreen()
                            print ("Erinaceous-flux Index Service Warning")
                            print ("*"*35)
                            print ("")
                            print ("You must un-mount "+filename+" before mounting a new file.")
                            print ("Press enter to return to the main menu.")
                            input ()
                            ui()
                        if menuinput2 == (2) and flag == False:
                            clearscreen()
                            print ("Erinaceous-flux Index Service Warning")
                            print ("*"*35)
                            print ("")
                            print ("There is no file within the application to un-mount.")
                            print ("Press enter to return to the main menu")
                            input ()
                            ui()
                        if menuinput2 == (2) and flag == True:
                            unmount()
                        if menuinput2 == (3) and flag == False:
                            ui()
                        if menuinput2 == (3) and flag == True:
                            ui()
                        if (menuinput2 != 1 or 2 or 3) or (menuinput2 > 1) or (menuinput2 < 3) and flag == True:
                            print ("")
                            print ("Please enter a valid selection.")
                            print ("Pressing enter will return you to the main menu.")
                            input ()
                            ui()
                        if (menuinput2 != 1 or 2 or 3) or (menuinput2 > 1) or (menuinput2 < 3) and flag == False:
                            print ("")
                            print ("Please enter a valid selection.")
                            print ("Pressing enter will return you to the main menu.")
                            input ()
                            ui()
                    if menuinput == (2) and flag == False:
                        print ("There is no file mounted to the application.")
                        print ("Please mount a file before attempting any search options.")
                        print ("Press enter to return to the main menu")
                        input ()
                        ui()
                    if menuinput == (2) and flag == True:
                        search_engine()
                    if menuinput == (3):
                        clearscreen ()
                        print ("Erinaceous-flux Index Service: About")
                        print ("*"*35)
                        print ("")
                        print ("\n> The Erinaceous Flux Index Service is property of, provided, and designed by (during his first year of study) Leeds University student Callum Dempsey Leach.\n")
                        print ("")
                        print ("\n> The Erinaceous Flux Index Service is designed to allow the user to search through a text file as part of the module 'COMP 1036' within Leeds University (c. 2013).\n")
                        print ("")
                        print ("\n> The accepted database format is as follows: AUTHOR(S) (i.e: 'Leach, Callum Dempsey'; or Kia;Leach, multiple authors seperated by semi-colon)[tab]YEAR (i.e. 1993)[tab]TITLE[tab]JOURNAL (or place of publication).")
                        print ("")
                        print ("\n>For more information about the author or if you would like to contact him please visit www.Twitter.com/ErinaceousFlux.\n")
                        print ("")
                        print ("\n>For more information about Leeds University of if you would like to contact the institution please visit www.leeds.ac.uk (references valid 27th April 2013).\n")
                        print ("")
                        print ("\n>Last modified 03 May 2013. Version 1.0. For Python 3.0 or above only.")
                        print ("")
                        print ("Press the Enter key to return to the application.")
                        input ()
                        ui()
                    if menuinput == (4):
                        print("")
                        print("Goodbye.")
                        if flag == 1:
                            file.close()
                            sys.exit()
                        else:
                            sys.exit()
                    elif (menuinput != 1 or 2 or 3 or 4) or (menuinput > 1) or (menuinput < 4):
                        print ("")
                        print ("Please enter a valid selection.")
                        print ("Pressing enter will return you to the main menu.")
                        input ()
                        continue
                except ValueError:
                    print ("")
                    print ("Please enter a valid selection.")
                    print ("Pressing enter will return you to the main menu.")
                    input ()
                    continue
        print ("Success")
        break
    except:
        print ("Error writing UI or pathways. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1


#CHECK ERRORS
#Before initializing the program checks for errors. If there were any engine errors defining any variables .etc. engine error equals 1 and the program terminates
if engine_error == 1:
    print ("")
    print ("An error occurred initializing the application. See the above log for more details.")
    print ("Terminating.")
    raise SystemExit
else:
    print ("")
    print ("Initialization successful.")
    clearscreen()
    print ("")
    print ("")
ui()

