num=input("Enter a number : ")

length= len(num)
count=0
for i in range (length+1):
    n=int(num)%10
    if(n == 0):
        count=count +1
if(count>0):
    print(f"{num} is a duck number ")
else:
    print(f"{num} is not a duck number ")