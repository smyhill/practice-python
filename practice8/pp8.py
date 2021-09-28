# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

p1 = str(input('Please enter r for rock, p for paper or s for scissors: '))
while p1 != 'r' or p1 != 'p' or p1 != 's':
    print("please enter a valid option")
    p1 = input('Please enter r for rock, p for paper or s for scissors: ')
    if p1 == 'r' or p1 == 'p' or p1 == 's':
        break

