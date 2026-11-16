# # Question 6 – Car Information System
class Car:
    company = "Toyota"

    def __init__(self,model,price):
        self.model = model 
        self.price = price

    def display(self):
        print("Company:",Car.company)
        print("Model:",self.model)
        print("Price:",self.price)

c1 = Car("Fortuner",3500000)
c2 = Car("Innova",2500000)

c1.display()
c2.display()