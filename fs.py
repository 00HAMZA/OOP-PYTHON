import json

with open("example.txt", "a") as files:
    content = files.write("bonuuuuus\n")
with open("example.txt", "r") as files:
    print(files.read())
    user = {
        "name" : "hamza hasni",
        "age" : 23,
        "skills" : ["frontend", "backend"]
    }
    jsonData = json.dumps(user, indent=4)
    with open("exampel.json", "w") as file:
        json.dump(user, file)
    with open("example.txt", "r") as a:
        print(a.read());
try:
    number = int(input("enter a number :"))
    result = number / 2
    print(result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("you cannot divide by zero")
finally:
    print("the program finished")
def checkage(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
print(checkage(-1))
