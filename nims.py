"""Nims game program

This game relies on conditionals, 
basic python math operations such as addition, subtraction & modulus
print statements, and a while-loop

"""

# Game intro
print """ 
=========================================================================
                    Thanks for playing Nims!

The goal of the game is to not be the last player to pick up a stone.
A player during their turn can pick up between 1-10 stones during their 
turn

Setup: Player One will decide how many stones will be in the pile
       Player Two will make the first selection of stones

       Player One and Two will then take turns removing the stones
       from the pile until 1 stone remains

       The player that picks up the last stone loses the game
=========================================================================
"""


stones = int(raw_input("Player One: how many stones do you want start with (1-99): "))

if not 0 < stones < 100:
    print "that was an invalid number of stones"
    stones = int(raw_input("Player One: how many stones do you want start with (1-99): "))


number_of_turns = 0

# game mechanics
while (stones > 1):
    if (number_of_turns %2 != 0):
        remove_stones = int(raw_input("Player One, please enter how many stones you want to remove:"))
        if (remove_stones > 0) and (remove_stones <= 10) and (remove_stones <= stones):
            stones = stones - remove_stones
            
            # calculates number of turns
            number_of_turns +=1
            print "the number of stones remaining are %s" % stones
            print "this game has played %s turns" % number_of_turns

        else:
            print "Illegal move.  Try again."
            print "the number of stones remaining are %s" % stones
    else:
        remove_stones = int(raw_input("Player Two, please enter how many stones you want to remove:"))
        if (remove_stones> 0) and (remove_stones <= 10) and (remove_stones <= stones):
            stones = stones - remove_stones
            number_of_turns +=1
            print "the number of stones remaining are %s" % stones
            print "this game has played %s turns" % number_of_turns
        else:
            print "Illegal move.  Try again."
            print "the number of stones remaining are %s" % stones

winner = int(number_of_turns % 2)

if (winner != 1):
    print "%s stone remains" % stones
    print "Congratulations player 1"
else:
    "%s stone remains" % stones
    print "Congratulations player 2"

# TODO for students:
# possibilities for refactoring or adding complexity: 
# 
# refactoring:
# 1) there are some repetitious lines in the code, can you use variables
# to help the game mechanics look cleaner to look at
# 2) can you refactor the code to completely use functions 
# and a def main() function?
#
# adding complexity
# 2) an advanced version of nims is played with up to 4 different piles of stones
# implement new game mechanics where players decide how many piles of stones there are
# and decide the number of stones per heap
# (maybe cap the number of stone per pile to 25 stones)
#
# Some questions to consider:
# try implementing 2 piles before making the number of piles variable to 4
# How would you take input where a player can designate which pile they can choose from
# How would you design the running display how many stones there are per pile for the players?
# How do you keep a running total of stones? How do you determine when a player wins?
