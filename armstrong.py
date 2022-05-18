from ast import Pow
import numpy
num=input("Enter a number : ")
p = len(num)
num1=int(num)
arm=0
li=[]
for i in range(p+1):
    arm = arm + numpy.power(int(num1%10),p)
    num1= num1/10

if(arm == int(num)):
    print(f"{num} is a armstrong number.")
else:
    print(f"{num} is not a armstrong number.")
  
