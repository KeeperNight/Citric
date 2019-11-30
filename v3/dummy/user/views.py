from django.shortcuts import render

def user_home(request):
    return render(request,'user/home.html')

def user_login(request):
    return render(request,'user/user_login.html')

def user_signup(request):
    return render(request,'user/user_signup.html')

def update_progress(request):
    return render(request,'user/update_progress.html')

def user_account(request):
    return render(request,'user/user_account.html')