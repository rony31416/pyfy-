from django.shortcuts import render, redirect
from .models import Blog


def hello(request):
    return render(request, 'base.html')

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})

def new_blog(request):

    return render(request, 'blog_form.html', {'form_title': 'Add New Blog'})
