import random
class Game:
    def guess(self):
        number=20
        count=0
        while(True):
            user_input=int(input('\nEnter the number : '))
            if(user_input==number):
                print("\nCongrats !!! You Win !!!")
                count=count+1
                break
            elif(count<4):
                if(user_input>number):
                    print("\n******************\nEnter lower number ")
                else:
                    print("\n******************\nEnter greater number ")
                count=count+1
                print("\nRemining Chances : ",4-count)
                print("\n******************")
                continue
            elif(count==4):
                print("\nGame Over")
                break
    
    def snake_water_gun(self):
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

obj=Game()
if __name__ =='__main__':

    print("Choose the game : ")
    print("1. Guess The Number\n2. Snake Water Gun")
    choice=int(input())
    if(choice==1):
        print("Welcome\n")
        obj.guess()
    elif(choice==2):
        print("Welcome\n")
        obj.snake_water_gun()

        

        
