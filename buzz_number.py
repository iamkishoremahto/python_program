num= input("Enter a number : ")

length= len(num)
n=int(num)

last_number= n%10

if last_number == 7 or n%7 == 0:
    print(f"{num} is a buzz number")
else:
    print(f"{num} is not a buzz number ")
