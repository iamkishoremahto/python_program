from audioop import reverse


num = input("Enter a number : ")
length = len(num)

n = int(num)
rev=0
while(n>0):
    n2=n%10
    n = int(n/10 )
    rev = rev*10 + n2
    
print(rev)
if rev == int(num):
    print(f"{num} is a pallindrome number ")
else:
    print(f"{num} is not a pallindrome number ")