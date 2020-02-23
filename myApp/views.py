from django.shortcuts import render
from django.utils import timezone
from .models import User

def index(request):
    return render(request, 'blog/posts.html', {})

def meep(request):
    return render(request, 'about.html')