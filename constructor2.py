class Bike:
    def __init__(self,company,model,mileage,horse_power):
        self.company=company
        self.model=model
        self.mileage=mileage
        self.horse_power=horse_power
    def show_Bike_Details(self):
        print(f"Company Name : {self.company} ")
        print(f"Model No. : {self.model}")
        print(f"Mileage : {self.mileage}")
        print(f"Hourse Power : {self.horse_power}")

obj=Bike("Honda","Passion Pro","65 KM/L","300 cc")

obj.show_Bike_Details()