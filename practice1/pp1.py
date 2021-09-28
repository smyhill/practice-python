# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

current_year = 2021
name = input("Please enter your name: ")
age = input("Please enter your age: ")
years_until = 100 -int(age)
age_100 = 2021 + years_until
print('Hello ' + name + ' you will turn 100 in ' + str(age_100))