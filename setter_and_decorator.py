class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}.{lname}@vmokshagroup.com"

    def explain(self):
        return f"first name is {self.fname} and last name is {self.lname}"
    @property # use by property we no need to use function
    def email(self):
        if self.fname== None or self.lname == None:
            return("Email is deleted")
        return f"{self.fname}.{self.lname}@vmokshagroup.com"

    @email.setter
    def email(self,string):
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
    

kishore=employee("kishore","mahto")

#print(kishore.explain())
kishore.fname="suresh"
#print(kishore.email)
kishore.email="Nitesh.Kumar@vmokshagroup.com"
#print(kishore.email)
del kishore.email
print(kishore.email)

kishore.email="kishore.kumar@vmokshagroup.com"
print(kishore.email)

