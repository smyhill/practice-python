# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
b= []

def FirstLast(a,b):
    list_length = len(a)
    b.append(a[0])
    b.append(a[list_length - 1])
    print(b)


