from django.shortcuts import render

def home(request):
    return render(request,'user/home.html')

def about_user(request):
    return render(request,'user/login.html')

def user_login(request):
    return render(request,'user/login.html')

def user_signup(request):
    return render(request,'user/signup.html')

def update_progress(request):
    return render(request,'user/update_progress.html')