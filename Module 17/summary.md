# Django Templating, Inheritance, Loop, Logic & Dynamic Routing

This document explains the core Django templating concepts with detailed examples and explanations.

---

## 📄 1. Django Templating

Django uses a powerful template engine to separate the presentation layer (HTML) from the business logic (Python).

### 🔧 Syntax

* `{{ variable }}` → Output a variable.
* `{% tag %}` → Used for logic like conditions or loops.

### 📁 Example:

```html
<!-- templates/hello.html -->
<h1>Hello, {{ name }}!</h1>
```

### 📘 views.py

```python
from django.shortcuts import render

def hello(request):
    context = {'name': 'Bangladesh'}
    return render(request, 'hello.html', context)
```

---

## 🧬 2. Template Inheritance

Django allows templates to inherit from a base template to maintain DRY principles.

### 📁 base.html

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header><h1>Welcome to My Site</h1></header>
    {% block content %}{% endblock %}
</body>
</html>
```

### 📁 home.html

```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<p>This is the home page content.</p>
{% endblock %}
```

### 📘 views.py

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

---

## 🔁 3. Loop in Template

Used for displaying lists.

### 📁 product\_list.html

```html
<h2>Product List:</h2>
<ul>
{% for product in products %}
    <li>{{ product }}</li>
{% empty %}
    <li>No products available.</li>
{% endfor %}
</ul>
```

### 📘 views.py

```python
from django.shortcuts import render

def products(request):
    product_list = ['Laptop', 'Phone', 'Tablet']
    return render(request, 'product_list.html', {'products': product_list})
```

---

## 🔍 4. Logic in Template

Templates support `if`, `elif`, `else` for basic logic.

### 📁 logic.html

```html
{% if is_logged_in %}
    <p>Welcome, user!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

### 📘 views.py

```python
from django.shortcuts import render

def login_status(request):
    context = {'is_logged_in': True}
    return render(request, 'logic.html', context)
```

---

## 🌐 5. Dynamic Routing with URL Parameters

Allows passing data via URL.

### 📁 urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('greet/<str:name>/', views.greet, name='greet'),
]
```

### 📘 views.py

```python
from django.shortcuts import render

def greet(request, name):
    return render(request, 'hello.html', {'name': name})
```

### 🔗 URL Example

```
http://127.0.0.1:8000/greet/rony/
```

Outputs: `Hello, rony!`

---

## ✅ Summary

| Feature         | Purpose                             |
| --------------- | ----------------------------------- |
| Templating      | Dynamic HTML rendering              |
| Inheritance     | DRY & reusable layouts              |
| Loop            | Render list items dynamically       |
| Logic           | Conditional rendering               |
| Dynamic Routing | URL parameter-based dynamic content |

---
