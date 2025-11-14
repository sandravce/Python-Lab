class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
            print("My car is a",self.color,self.brand)
c1=car("Mercedes","Black")
c2=car("Lamborghini","Blue")
c1.display()
c2.display()
