num=int(input("Enter the limit of fibonaci series : "))
#0 1 1 2 3 
def fibonacci(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

for i in range(num):
    print(fibonacci(i), end=" ")
