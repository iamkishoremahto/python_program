number=20
count=1
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
