def getinput():
    a=int(input('\nEnter the value of a :'))
    b=int(input('\nEnter the value of b : '))
    return a,b

def add():
    a,b=getinput()
    return a+b

def sub():
    a,b=getinput()
    return a-b

def mul():
    a,b=getinput()
    return a*b

def div():
    a,b=getinput()
    return a/b

print(''' 
1. add
2. sub
3. mul
4. sub''')

choice=int(input('Enter your choice: '))
operation=[add,sub,mul,div]
result=int((operation[choice-1])())
print('Ans : ',result)
 





