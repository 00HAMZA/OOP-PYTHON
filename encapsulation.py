class Person:
    def __init__(self, name, age, gender):
        self.name = name # Public
        self._age = age # Protected
        self.__gender = gender #Private
    @property
    def gandora(self):
        return self.__gender
    @gandora.setter
    def gandora(self, newGender):
        self.__gender += newGender
        if(newGender > 100):
            return print("invalid number")
        return self.__gender
    
p1 = Person("hamza", 12, 10)
print(p1.name, p1._age)
#print(p1.getter())
#print(p1.setter())
ss = p1.gandora = 20 
print(ss)
