from operator import truediv


n=int(input('Enter the no of lines : '))
condition=input('Enter the condition in true or false : ')
def con(condition):
    con=condition
    if(con=="true" or con=="True" or con=="TRUE"):
        return True
    else:
        return False

if(con(condition)):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
else:
    for i in range(0,n):
        for j in range(i-1,n-1):
            print("*", end="")
        print("\r")
