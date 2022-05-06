class A:
    def Class_A(self):
        print("I am from class A. ")

class B:
    def Class_B(self):
        print("I am from Class B.")
class C(A,B):
    def Class_C(self):
        print("I am from Class C.")

obj=C()
obj.Class_A()
obj.Class_B()
obj.Class_C()


