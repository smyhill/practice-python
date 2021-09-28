# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
import random

a_start = random.randint(1,10)
a_end = random.randint(15000,20000)
b_start = random.randint(1,10)
b_end = random.randint(15000,20000)

a = []              
b = []
c = []

def GenRandomList(start,end,ranlist):
    """Generates a random list between arg 1 and arg 2 and appends the values to a list that is arg c """
    while start < end:
        ranlist.append(start)
        iterator = random.randint(1,100)
        start += iterator

GenRandomList(a_start,a_end,a)
GenRandomList(b_start,b_end,b)

for i in a:
    bool1 = i in b
    bool2 = i in c
    if bool1 == True and bool2 == False:
        c.append(i)
print(c)

