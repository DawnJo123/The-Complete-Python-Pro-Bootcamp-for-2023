#Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the tresure.")
choice1=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'. ")

if choice1=='left':
        choice2=input("You have come to a lake. Ther is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim accros. ")
        if choice2=='wait':
              choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
              if choice3=='red':
                    print("This room is full of fire. Game Over")
              elif choice3=='yellow':
                    print("You found the treasure! You win!")
              else:
                    print("You chose a door that doesn't exist. Game Over")
        else:
              print("You get attacked by an angry trout. Game over")
else:
   print("YOu fell into a hole.Game Over")