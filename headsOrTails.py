#Generating Heads or Tails using random module
import random

#random.randint(a,b) is used to generate integers randomly between a and b including both.
num=random.randint(0,1)
if num==0:
    print("Tails")
else:
    print("Heads")
