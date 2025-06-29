from django.shortcuts import render

from django.http import HttpResponse

def hello(request) :
    return HttpResponse("Hello Django!")

def base(request) :
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')

def products(request) :
    return render(request,'products.html')

def login(request): 
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def contact(request): 
    return render(request, 'contract.html')

def about(request):
    return render(request, 'about.html')

def categories(request):
    return render(request, 'catagories.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')  # You can create this template later


# Create your views here.
