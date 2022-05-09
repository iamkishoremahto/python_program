class student:
    _ans=9
    __b=10
    def __init__(self,sname,sClass,sroll):
        self.name=sname
        self.Class=sClass
        self.roll=sroll
    
    def show_Details(self):
        print(f"Name of the student : {self.name}\nRoll No. : {self.roll}\n Class : {self.Class}")

    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod

    def greeting(string):
        print("Good Morning ",string)

kishore=student.from_str("Kishore-B.Tech-17/cse/368")
print (kishore.name)
kishore.greeting("Rohan")
st=student("Kishore","II",56)
print(st._ans)
print(st._student__b)
