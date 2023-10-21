#Love calculator

print("The Love Calculator is calculating your score.... ")
name1=input("Enter your name? ")
name2=input("Enter their name? ")
combined=name1+name2
lowercase=combined.lower()
T=lowercase.count('t')
R=lowercase.count('r')
U=lowercase.count('u')
E=lowercase.count('e')
firstDigit=T+R+U+E

L=lowercase.count('l')
O=lowercase.count('o')
V=lowercase.count('v')
E=lowercase.count('e')
secondDigit=L+O+V+E
totalScore=firstDigit*10 + secondDigit


if totalScore<10 or totalScore>90:
    print(f"Your score is {totalScore},you are like coke and mentos")
elif totalScore>=40 and totalScore<=50:
    print(f"Total Score is {totalScore}, your are alright together. ")
else:
    print(f"Your score is {totalScore}.")