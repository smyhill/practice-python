# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
def FibonnaciGenerator(first_num,sequence_len):
    fibonacci = []
    if sequence_len > 1:
        iterator = 1
        fibonacci.append(first_num)
        fibonacci.append(first_num)
        while (iterator + 1) < sequence_len:
            current_num = fibonacci[iterator] + fibonacci[iterator - 1]
            fibonacci.append(current_num)
            iterator += 1
    else:
        fibonacci.append(first_num)      
    print(fibonacci)

fib_len = int(input("Please enter the length of the fibonacci sequence you would like to generate: "))
start_num = int(input("Please enter the first number of the Fibonacci sequence you would like to generate: "))

FibonnaciGenerator(start_num,fib_len)