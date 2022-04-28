num=int(input('Enter a number : '))

while(True):
    if(num>100):
        print("Congrats ! you enter a number greater then 100")
        break
    if(num<=100):
        print("Try Again")
        num=int(input('Enter a number : '))
        continue