
---

# 🧱 Python Modules and Packages – A Complete Guide

This note explains **creating & using your own modules**, **using built-in modules**, **installing and using external packages with pip**, and an **overview of the Python Standard Library**.

---

## 📦 1. Creating and Using Modules

### 🔹 What is a Module?

A **module** is a file containing Python code (.py) that can define functions, classes, and variables. It helps organize and reuse code.

---

### 🔧 How to Create a Module?

```python
# File: mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

pi = 3.1416
```

---

### 📥 How to Use the Module?

```python
# File: main.py

import mymodule

print(mymodule.greet("Rony"))          # Hello, Rony!
print(mymodule.add(10, 5))             # 15
print(mymodule.pi)                     # 3.1416
```

---

### 🎯 Import Variations

```python
from mymodule import greet, pi

print(greet("ChatGPT"))
print(pi)

import mymodule as mm

print(mm.add(2, 3))
```

---

## 📚 2. Using Built-in Modules

Python has many built-in modules to perform common tasks.

---

### ✅ Examples:

#### 1. `math` – Mathematical operations

```python
import math

print(math.sqrt(16))      # 4.0
print(math.factorial(5))  # 120
print(math.pi)            # 3.141592653589793
```

---

#### 2. `random` – Randomization

```python
import random

print(random.randint(1, 10))      # Random int between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random element
```

---

#### 3. `datetime` – Date and Time

```python
import datetime

now = datetime.datetime.now()
print(now)                         # 2025-06-22 16:45:00
print(now.strftime("%Y-%m-%d"))    # '2025-06-22'
```

---

#### 4. `os` – Interacting with the Operating System

```python
import os

print(os.getcwd())       # Get current working directory
print(os.listdir())      # List files in current directory
```

---

## 📦 3. Installing and Using Packages with `pip`

### 🔹 What is pip?

`pip` is the package installer for Python. It allows you to install and manage external libraries.

---

### ✅ Install a Package:

```bash
pip install requests
```

---

### 🔍 Check Installed Packages:

```bash
pip list
```

---

### ❌ Uninstall a Package:

```bash
pip uninstall requests
```

---

### 🧪 Using Installed Package:

```python
import requests

res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())  # Prints GitHub API JSON response
```

---

## 📘 4. Python Standard Library Overview

Python ships with a massive set of modules (no installation required). These include:

| Module        | Description                          | Example Use                  |
| ------------- | ------------------------------------ | ---------------------------- |
| `math`        | Math functions                       | `math.sqrt(25)`              |
| `random`      | Random number generation             | `random.randint(1, 100)`     |
| `datetime`    | Date and time operations             | `datetime.datetime.now()`    |
| `os`          | OS interactions                      | `os.getcwd()`                |
| `sys`         | Python runtime environment           | `sys.version`                |
| `json`        | Work with JSON data                  | `json.loads()`               |
| `re`          | Regular expressions                  | `re.match(pattern, string)`  |
| `time`        | Time-related functions               | `time.sleep(2)`              |
| `collections` | High-performance container datatypes | `collections.Counter()`      |
| `itertools`   | Iterator building blocks             | `itertools.combinations()`   |
| `statistics`  | Statistical functions                | `statistics.mean([1, 2, 3])` |
| `http`        | HTTP clients and servers             | `http.client`, `http.server` |

---

### 📌 Example: Working with JSON

```python
import json

data = '{"name": "Rony", "age": 23}'
parsed = json.loads(data)

print(parsed['name'])  # Rony
```

---

### 🧪 Example: Using `collections.Counter`

```python
from collections import Counter

text = "hello world"
counter = Counter(text)

print(counter)  # Counts each character
```

---

## ✅ Summary

| Concept          | Key Point                                  |
| ---------------- | ------------------------------------------ |
| Modules          | Code reuse; `.py` files with definitions   |
| Built-in Modules | Included with Python (math, os, random...) |
| pip              | Install and manage external packages       |
| Standard Library | Rich collection of useful built-in modules |

---
