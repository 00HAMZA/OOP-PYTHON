class Animal:
    def __init__(self):
        pass
    def makeSound(self):
        print("some animal sound")

class Dog(Animal):
    def makeSound(self):
        print("whoof whoof")

class Cat(Animal):
    def makeSound(self):
       print("meow meow")
        
dog1 = Dog()
dog1.makeSound()
cat1 = Cat()
cat1.makeSound()

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
calc = Calculator()

print(calc.add(1 + 2 + 2))