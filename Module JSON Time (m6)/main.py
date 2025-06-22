"""# File: main.py

import mymodule

print(mymodule.greet("Rony"))          # Hello, Rony!
print(mymodule.add(10, 5))             # 15
print(mymodule.pi)                     # 3.1416


from mymodule import greet, pi

print(greet("ChatGPT"))
print(pi)

import mymodule as mm

print(mm.add(2, 3))



import math

print(math.sqrt(16))      # 4.0
print(math.factorial(5))  # 120
print(math.pi)            # 3.141592653589793




import random

print(random.randint(1, 10))      # Random int between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random element





import datetime

now = datetime.datetime.now()
print(now)                         # 2025-06-22 16:45:00
print(now.strftime("%Y-%m-%d"))    # '2025-06-22'




import os

print(os.getcwd())       # Get current working directory
print(os.listdir())      # List files in current directory


"""



import requests

res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())  # Prints GitHub API JSON response