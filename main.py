import  math
import random
from datetime import datetime
import requests
response = requests.get("https://www.youtube.com/")
print(response.apparent_encoding)
print(math.sqrt(4))
print(math.pi)
print(math.pow(2, 3))
number =  random.randint(1, 10)
print(number)
currentTime = datetime.now()
print(currentTime)
