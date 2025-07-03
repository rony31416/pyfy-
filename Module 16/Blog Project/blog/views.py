from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog
from .forms import BlogForm


def hello(request):
    return render(request, 'base.html')


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})


def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog created successfully!')
            return redirect('home')
    else:
        form = BlogForm()
    
    return render(request, 'blog_form.html', {
        'form': form,
        'form_title': 'Add New Blog'
    })


def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blog_form.html', {
        'form': form,
        'form_title': 'Edit Blog'
    })


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        return redirect('home')
    
    return render(request, 'confirm_delete.html', {'blog': blog})