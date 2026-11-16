# Question 8 – Inheritance (Person and Student)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,roll):
        super().__init__(name, age)
        self.roll = roll

    def display_student(self):
        self.display_person()
        print("Roll Number:",self.roll)

s1 = Student("Sanjana",22,101)
s1.display_student()
