class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept = dept
    
    def display(self):
        print("Name:",self.name)
        print("salary :",self.salary)
        print("Dept:",self.dept)

m1 = Manager("Sanjana",50000,"IT")
m1.display()