class Student:
    count = 10
    def __init__(self, user, gpa):
        self.user = user
        self.gpa = gpa
    @classmethod
    def countUsers(cls):
        print(f"we have {cls.count} users")
    @staticmethod
    def sayHello():
        print("hello from static method")

student1 = Student("hamza", 12);
print(student1.user)
print(student1.gpa)
student1.countUsers()
student1.sayHello()