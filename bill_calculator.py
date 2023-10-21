#Bill per person is calculated based on the total amount, tip percentage and totla number of people
print("Welcome to the Bill Calculator")
bill=float(input("What was the totla bill ? $"))
percentage=int(input("What percentage tip would you like to give ? 10, 12 or 15? "))
people=int(input("How many people to split the bill with ? "))
total=bill*(1+percentage/100)

perPerson=total/people
print("Each person should pay: ",round(perPerson,2))