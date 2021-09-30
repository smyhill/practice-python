# Ask the user for a number and determine whether the number is prime or not.
x = int(input("Please enter an integer to check if prime: "))
a = list(range(2,x))
divisor_list = []
for i in a:
    if x % i == 0:
        divisor_list.append(i)
if divisor_list:
    print(str(x) + " is not a prime number the following are its divisors: ")
    print(divisor_list)
else:
    print(str(x) + " is a prime number!")

# wrapped in function to check whether the number is prime or not.
def CheckIfPrime(x):
    a = list(range(2,x))
    divisor_list = []
    for i in a:
        if x % i == 0:
            divisor_list.append(i)
    if divisor_list:
        print(str(x) + " is not a prime number the following are its divisors: ")
        print(divisor_list)
    else:
        print(str(x) + " is a prime number!")
