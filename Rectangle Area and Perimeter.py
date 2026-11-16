# # Question 5 – Rectangle Area and Perimeter

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def cal_area(self):
        return self.length * self.width

    def cal_perimeter(self):
        return 2*(self.length + self.width)

    def display(self):
        print("Area :", self.cal_area())
        print("Perimeter :", self.cal_perimeter())

r1 = Rectangle(10,5)
r1.display()
    
