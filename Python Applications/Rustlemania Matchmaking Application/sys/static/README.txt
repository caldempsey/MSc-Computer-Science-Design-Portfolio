======================
Rustlemania Matchmaking Application v. release.2.3.
----------------------
                 _
             ,.-" "-.,
            /   ===   \
           /  =======  \
        __|  (o)   (0)  |__      
       / _|    .---.    |_ \         
      | /.----/ O O \----.\ |       
       \/     |     |     \/        
       |                   |            
       |                   |           
       |                   |          
       _\   -.,_____,.-   /_         
   ,.-"  "-.,_________,.-"  "-.,
  /          |       |          \  
 |           l.     .l           | 
 |            |     |            |
 l.           |     |           .l             
  |           l.   .l           | \,     
  l.           |   |           .l   \,    
   |           |   |           |      \,  
   l.          |   |          .l        |
    |          |   |          |         |
    |          |---|          |         |
    |          |   |          |         |
    /"-.,__,.-"\   /"-.,__,.-"\"-.,_,.-"\
   |            \ /            |         |
   |             |             |         |
    \__|__|__|__/ \__|__|__|__/ \_|__|__/

======================
Rustlemania Matchmaking Application v. release.2.3.
======================

======================
About this application...
----------------------

The Rustlemania is a monthly tournament hosted on www.destiny.gg for the www.destiny.gg community.
The Rustlemania often spans between tens to hundreds of competitors.

This matchmaking service was written for the community at www.destiny.gg to help create and organize tournaments spanning several hundreds of players.
To do this the matchmaking service uses a value players give which identifies their subjective belief of where they stand relative to other players. 
The matchmaking service also takes the objective rank of each player determined by the appropriate product (Counter strike ranks, dota 2 ranks, chess ELO .etc.).
From these details the service calculates all possible teams of those players such that they reach an average rank (appends these to the database).
You can export these results using the search function in the application.

======================
What you need to input...
----------------------

The matchmaking service requires a database of players as input in '\sys\lib', which must contain the following details seperated by the '|' character.
"<PlayerName>|<SteamURL>|<Rank>|<Powerlevel>"

Legend
======================
Player name = The name of the player.
SteamURL = Can be any URL which can identify contact to the player (but destiny.gg users use the steamgroup).
Rank = Objective rank (as in Ranks.txt).
Powerlevel = Subjective skill rating (usually out of 10) in relation to other players.
----------------------

The matchmaking service requires the objective rank of each player.
For this list of possible ranks must be given in ascending to descending order in the RANKS.txt file within '/sys/cfg'. 

You can also "find and replace" ranks using the following format...
======================
OLDRANK|NEWRANK
---------------------
BPR|BEST PLAYER RANK
WPR|WORST PLAYER RANK
---------------------

The best rank, given as BEST PLAYER RANK, will determine the best players whilst players assigned WORST PLAYER RANK will determine the worst players.
Using this system the "true rank" of each player is a calculated average of the player's subjective powerlevel and their actual rank. 
The true rank, or powerlevel, is the value used by the application to matchmake players. 

=====================
To do list...
---------------------
1. Allow the database columns to be determined by information given in each field within the first line of the text file (for customization).