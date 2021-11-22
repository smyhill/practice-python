# Take a list and write a program that prints out all the elements of the list that are less than 5.
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

list = [1, 1, 2, 2, 3, 5, 9, 15, 27, 43, 66, 79]
less_than_7_list = []
threshold = input("Please enter a threshold: ")
for i in list:
    if i < int(threshold):
        less_than_7_list.append(i)
print(less_than_7_list)
