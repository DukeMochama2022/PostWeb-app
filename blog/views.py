from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts=Post.objects.all().order_by('-date_posted')
    
    context={
        'posts':posts
    }
    return render(request, "blog/index.html",context)

def about(request):
    return render(request,'blog/about.html')