class Personal_info:
    def __init__(self,name,dob,address,mob):
        self.name=name
        self.dob=dob
        self.address=address
        self.mob=mob
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Date Of Birth : {self.dob}")
        print(f"Address : {self.address}")
        print(f"Mobile No. : {self.mob}")

p=Personal_info("Kishore","15/09/2000","Godda",8340317197)
p.showDetails()
