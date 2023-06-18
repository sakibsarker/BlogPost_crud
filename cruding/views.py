from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .urls import path
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,"index.html",{'posts':posts})
def post(request,num):
    posts=Post.objects.get(id=num)
    return render(request,"post.html",{'posts':posts})