#Password Generator (shuffled letters, symbols and numbers)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
noOfLetters=int(input("How many letters would you like in your password? "))
noOfSymbols=int(input("How many symbols would you like in your password? "))
noOfNumbers=int(input("How many numbers would you like in your password? "))

# A list is needed inorder to store the randomly generated letters, symbols and nnumbers.
password_list=[]

# Each for loop generate a random letter, symbols, numbers respectively and store it in the list likewise.
for i in range(0,noOfLetters):
    password_list+=random.choice(letters)

for j in range(0,noOfSymbols):
    password_list.append(random.choice(symbols))

for k in range(0,noOfNumbers):
        password_list.append(random.choice(numbers))

# Astring to store the list elements when printed randomly
passwordFinal=''

for x in password_list:
     pwdStr=   random.choice(password_list)
     passwordFinal+=pwdStr

print(passwordFinal)