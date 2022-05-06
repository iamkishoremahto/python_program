class A:
    def Class_A(self):
        print("I am from class A.")

class B(A):
    def Class_B(self):
        print("I am from class B.")

obj=B()
obj.Class_A()
obj.Class_B()