# Question 9 – Method Overriding -- (Intermediate) (Inheritance)
class Animal:
    def sound(self):
        print("Animal Makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
    
a1 = Animal()
d1 = Dog()

a1.sound()
d1.sound()