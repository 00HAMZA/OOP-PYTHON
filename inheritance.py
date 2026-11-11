class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def makeSound(self):
        print("halala w yalala")
        


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


student = Student("Hamza", 20, 15)

print(student.name)
print(student.age)
print(student.grade)
student.makeSound()