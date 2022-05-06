class A:
    def Class_A(self):
        print("I am from class a")

class B(A):
    def Class_B(self):
        print("I am from class b")

class C(B):
    def Class_C(self):
        print("I am from class c")

obj=C()

obj.Class_A()
obj.Class_B()
obj.Class_C()