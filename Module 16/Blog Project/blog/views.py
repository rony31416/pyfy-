from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def hello(request):
    # posts = Post.objects.all()
    
    # result = ""
    
    # for post in posts :
    #     result += f"{post.title} - {post.content} - {post.created_at}<br>"
    # return HttpResponse(result)  
    return render(request, 'index.html')