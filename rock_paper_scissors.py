rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Rock Paper Scissors")
user=int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print("Your choice:")
print("------------")
if user==0:
    print(rock)
elif user==1:
    print(paper)
else:
    print(scissors)

comp=random.randint(0,2)
print("         ")
print("Computer's choice:")
print("------------------")
if comp==0:
    print(rock)
elif comp==1:
    print(paper)
else:
    print(scissors)

if comp==user:
    print("Draw")
elif comp==2 and user==0:
    print("You win")
elif user==1 and comp==0:
     print("You win")
elif user==2 and comp==1:
    print("You win")

else:
    print("You lose")
