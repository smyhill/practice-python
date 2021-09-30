# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# Extras: 
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

def game_loop():
    ran_num = random.randint(1,9)

    guess = 100
    counter = 0
    while guess != ran_num:
        guess = int(input('Enter your guess for the random number: '))
        counter += 1
        if guess > ran_num:
            print("Your guess was too high, try again")
        else:
            print("Your guess was too low, try again")     

    print("You Guessed Correctly! The random number was " + str(ran_num) + " and it took you only " + str(counter) + " tries!")

game_loop()

yn = "Y"
while yn == "Y":
    game_loop()
    yn = input('Would you like to play again? Y/N: ')
print("Thank you for playing, goodbye")