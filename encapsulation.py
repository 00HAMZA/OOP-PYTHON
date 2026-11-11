class Person:
    def __init__(self, name, age, gender):
        self.name = name # Public
        self._age = age # Protected
        self.__gender = gender #Private
    def getter(self):
        return self.__gender
    def setter(self):
        self.__gender += 10
        return self.__gender
    
p1 = Person("hamza", 12, 10)
print(p1.name, p1._age)
print(p1.getter())
print(p1.setter())