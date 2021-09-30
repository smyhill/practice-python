# Print the numbers from 1 to 100 inclusive, each on their own line.
# If, however, the number is a multiple of three then print Fizz instead, and if the number is a multiple of five then print Buzz.
# For numbers which are multiples of both three and five then print FizzBuzz.



for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
