# Take two lists, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. Write this using at least one list comprehension.
import random

def CreateRandomList(Random_List):
    """ 
    Populates a random, sorted list between 15 and 50 values long. Values are <= 1000.
    """
    iterator = 0
    list_len = random.randint(15,50)
    while iterator < list_len:
        ran_val = random.randint(1,1000)
        Random_List.append(ran_val)
        iterator += 1
    Random_List = Random_List.sort()

a=[]
b=[]
CreateRandomList(a)
CreateRandomList(b)

c = [i for i in a if i in b]
print(c)