num=int(input('Enter last num'))


def fibonacci(num):
    first=0
    second=1
    print("0 1  ", end="")
    for i in range(num):
       
        next_num=first+second
        first=second
        second= next_num
        print(next_num, end=" ")
    
    
print(fibonacci(num))