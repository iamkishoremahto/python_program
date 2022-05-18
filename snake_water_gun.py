import random

computerWin=0
userWin=0
n=10
while(n>0):
    list=("Snake","Water","Gun")
    user=input("Enter your choice (Snake, Water, Gun) : ")
    computer=random.choice(list)
    if(user=="Snake" and computer=="Water"):
        print("You are winner !!!")
        userWin=userWin+1
    elif(user=="Water" and computer=="Gun"):
        print("You are winner !!!")
        userWin=userWin+1
    elif(user=="Gun" and computer=="Snake"):
        print("You are winner !!!")
        userWin=userWin+1
    elif(computer=="Snake" and user=="Water"):
        print("computer is winner !!!")
        computerWin=computerWin+1
    elif(computer=="Water" and user=="Gun"):
        print("computer is winner !!!")
        computerWin=computerWin+1
    elif(computer=="Gun" and user=="Snake"):
        print("computer is winner !!!")
        computerWin=computerWin+1
    elif(computer==user):
        print("Both choices are equal")
    n=n-1

if(userWin>computerWin):
    print("You are winner !!!")
    print("Total user win : ",userWin)
    print("Total Computer win : ",computerWin)
elif(userWin==computerWin):
    print("Both are Winner !!!")
    print("Total user win : ",userWin)
    print("Total Computer win : ",computerWin)
else:
    print("computer is winner !!!")
    print("You are lost !!! Try next time ")

    print("Total user win : ",userWin)
    print("Total Computer win : ",computerWin)

    