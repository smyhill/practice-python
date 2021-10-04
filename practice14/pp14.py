# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1,2,2,1,3,4,5,5,4,3,6,7,8,7,9,]
b = []
def FindDuplicates(input_list,output_list):
    output_list = set(input_list)
    output_list = list(output_list)
    return output_list

print(FindDuplicates(a,b))