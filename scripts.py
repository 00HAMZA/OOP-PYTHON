class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def brake(self):
        print("whoof whoof")

class Owner:
    def __init__(self, name, contact, adress):
        self.name = name
        self.contact = contact
        self.adress = adress
    
        
owner1 = Owner("hamza", "sale", "888")
dog1 = Dog("3ayoucha", "scotich", owner1)
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)
print(dog1.owner.contact)
print(dog1.owner.adress)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def accelerate(self):
        self.grade += 10
    def showSpeed(self):
        print(self.grade)

student1 = Student("hamza", 9)
student1.accelerate()
student1.showSpeed()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def displayInfo(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
    
    def updateEmail(self, newEmail):
        self.email = newEmail
        print("Email updtaed succefully")
    
user1 = User("hamza", "hamzalawi3@gmail.com")

user1.displayInfo()
user1.updateEmail("trading2020hamz@gmail.com")
user1.displayInfo()