from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
   name = "Rony's Web Page "
   return render(request, 'index.html', {'name' : name})

# Create your views here.
