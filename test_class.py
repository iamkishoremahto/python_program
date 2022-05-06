from turtle import color


class Mobile:
    def get_color(self,color):
        self.color=color
    def get_model(self,model):
        self.model=model
    def ring(self):
        print("Calling")

    def show_color(self):
        print("The color is : ",self.color)
    def show_model(self):
        print("Model : ",self.model)

obj1=Mobile()
obj1.get_color("Red")
obj1.get_model("MI Y1")
obj1.show_color()
obj1.show_model()
