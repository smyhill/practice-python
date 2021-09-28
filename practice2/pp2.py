# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num  = float(input('Please enter a number: '))
mod = num % 2
m4 = num % 4
if m4 == 0:
    print('Your number ' + str(num) + " is a multiple of 4 and even")
else:   
    if mod == 0:
        print('Your number ' + str(num) + " is even")
    else:
        print('Your number ' + str(num) + " is odd")
