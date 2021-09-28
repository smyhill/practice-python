# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

def rpc():
    p1 = str(input('Player 1: please enter r for rock, p for paper or s for scissors: '))
    p2 = str(input('Player 2: please enter r for rock, p for paper or s for scissors: '))

    while p1 == 'r':
        if p2 == 'r':
            print("Both players chose Rock: Tie!")
            break
        elif p2 == 'p':
            print("Paper Beats Rock: Player 2 Wins!")
            break
        else:
            print("Rock Beats Scissors: Player 1 Wins!")
            break    

    while p1 == 'p':
        if p2 == 'r':
            print("Paper Beats Rock: Player 1 Wins!")
            break
        elif p2 == 'p':
            print("Both Players Chose Paper: Tie!")
            break
        else:
            print("Scissors Beats Paper: Player 2 Wins!")
            break  
        
    while p1 == 's':
        if p2 == 'r':
            print("Rock Beats Scissors: Player 2 Wins!")
            break
        elif p2 == 'p':
            print("Scissors Beats Paper: Player 1 Wins!")
            break
        else:
            print(" Both Players Chose Scissors: Tie!")
            break  
    print("Play Again?")
rpc()

yn = input('Type "Y" to play again or "N" to quit: ')
while yn == "y":
    rpc()
    yn = input('Type "Y" to play again or "N" to quit: ')


