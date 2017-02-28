print """ 
=========================================================================
                    Thanks for playing Nims Refactored!

The goal of the game is to not be the last player to take a bottle of 
beer down from the wall.
A player take down between 1-10 beers during their turn

Setup: Player One will decide how many bottles of beer are on the wall
       Player Two will make the first selection of beers

       Player One and Two will then take turns removing the beers
       from the wall until 1 beer remains

       The player that takes down the last beer loses the game
=========================================================================
"""
beers = int(raw_input("""Player One: How many bottles of beer on the wall should
    we start with: choose between 1 and 99"""))
if not 0 < beers < 100:
    print "that's the wrong number of beers"

number_of_turns = 0

while (beers > 1):
    if (number_of_turns %2 != 0):
        remove_beers
