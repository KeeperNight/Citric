from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'author/home.html')

def about_author(request):
    return render(request,'author/login.html')

def author_login(request):
    return render(request,'author/login.html')

def author_signup(request):
    return render(request,'author/signup.html')