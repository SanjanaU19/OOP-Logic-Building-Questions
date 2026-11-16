## Question 2 – Employee Salary Calculator
class Employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        print("Employee Name :",self.name)
        print("Annual Salary : ",self.monthly_salary * 12)

e1 = Employee("sanjana",40000)
e1.annual_salary()