from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.



def hello(request):
    return HttpResponse(
       "<h1>Hello Wolrd!!</h1>"
    )



def dashboard(request):
    return HttpResponse(
        "<h2>This is my dummy dashboard </h2> "
    )