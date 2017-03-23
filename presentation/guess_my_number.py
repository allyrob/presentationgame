import random

ROUND = 0

def play_game(low_num, high_num, name):
    player_correct = False
    guesses_taken = 0
    number = random.randint(low_num, high_num)
    print "Guess a number between %s and %s" %(low_num, high_num)

    while guesses_taken < 5 and not player_correct:
        print "Take a guess!"
        guess = input()
        guess = int(guess)

        guesses_taken = guesses_taken + 1

        if guess < number:
            print "Your guess is too low..."

        elif guess > number:
            print "Your guess is too high..."

        else:
            player_correct = True
            print "Way to go %s! You guessed the correct number in %s guesses" % (name, 
            str(guesses_taken))
        

    if guesses_taken > 5 and guess != number: 
        number = str(number)    
        print "Nope. The number I was thinkking of was %s" % number
        print "Better luck next time!"

def main():
    ROUND = 0
    name = raw_input('Name: ')
    play = raw_input("Want to play a game: y/n: ")
    while play == "y":
        if ROUND < 1:
            play_game(1,10, name)
            again = raw_input("play again? y/n: ")
            if again == "y":
                ROUND =+ 1
            else:
                print "I said good day, sir"
                break
        else:
            play_game(1, (ROUND * 20), name)
            again = raw_input("play again? y/n: ")
            if again == "y":
                ROUND =+ 1
            else:
                print "I said good day, sir"
                break
    while play == "n":
        print "Thanks for playing"
        break



if __name__ == '__main__':
    main()
