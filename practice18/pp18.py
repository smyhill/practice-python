# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random
def GenRandomNumAsList(length):
    x = []
    i = 0
    while i < int(length):
        y = random.randint(0,9)
        x.append(y)
        i += 1
    return(x)

# print(GenRandomNumAsList())
difficulty = input("Please enter the game length: ")
x = GenRandomNumAsList(difficulty)



guess = input("Please enter your " + str(difficulty) + " digit guess: ")
guess_list = list(guess)
print(guess)
print(guess_list)
print(len(guess))
print(difficulty)
print(x)

def CowBullChecker(x, guess_list):
    cow_bull = []
    for digit in guess_list:
        iterator = 0
        if digit == x[iterator]:
            print(digit)
            print(x[iterator])
            cow_bull.append("cow")
        else:
            print(digit)
            print(x[iterator])
            cow_bull.append("bull")
    return(cow_bull)

cow_bull = CowBullChecker(x, guess_list)
print(cow_bull)
while ('bull' in cow_bull):
    guess = input("Please enter your " + str(difficulty) + " digit guess: ")
    guess_list = list(guess)
    cow_bull = CowBullChecker(x, guess_list)
    if 'bull' in cow_bull == False:
        print(cow_bull)
        break
    else:
        print(cow_bull)
        print('Guess is incorrect')

