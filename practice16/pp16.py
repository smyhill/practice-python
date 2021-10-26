# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import random

def PasswordGenerator(length = 12):
    characters = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")","_","-","+","=",":",";","<",">","?","~","/","|"]
    i = 0
    password = ""
    while i < length:
        a = str(random.choice(characters))
        password += a
        i += 1
    return password

print(PasswordGenerator(25))
