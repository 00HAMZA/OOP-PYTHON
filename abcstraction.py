from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    
    def make_sound(self):
       print("whoof")

class Cat(Animal):
    
    def make_sound(self):
        print("meow")
        
cat1 = Cat()
cat1.make_sound()
dog1 = Dog()
dog1.make_sound()
animal1 = Animal()
animal1.make_sound()