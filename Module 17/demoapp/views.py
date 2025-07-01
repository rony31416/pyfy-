from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


def home(request):
    
    person = {
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 30,
    "email": "alice.johnson@example.com",
    "is_employed": True,
    "address": {
        "street": "123 Maple Street",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62704"
        },
    "hobbies": ["reading", "cycling", "cooking"]
    }


    return render(request,"index.html", { 'person' : person})


