def user_input():
    num1=int(input("Enter the value of num1: "))
    num2=int(input("Enter the value of num2: "))
    return num1,num2

def add():
    a,b=user_input()
    
    if((a==56 and b==9) or (a==9 and b==56)):
        print("Ans : 77")
    else:
        result=a+b
        print("Ans : ",result)

def mul():
    a,b=user_input()
    
    if((a==45 and b==3) or (a==3 and b==45)):
        print("Ans : 555")
    else:
        result=a*b
        print("Ans : ",result)

def sub():
    a,b=user_input()
    result=a-b
    print("Ans : ",result)

def div():
    a,b=user_input()
    
    if((a==56 and b==6) or (a==6 and b==56)):
        print("Ans : 4")
    else:
        result=a/b
        print("Ans : ",result)
if __name__ =='__main__':

    print("""Enter your choice
    1. Add
    2. Mul
    3. Sub
    4. Div""")

    choice=int(input('Choice : '))
    Calculator=[add,mul,sub,div]
    output=(Calculator[choice-1])()
    print(output)