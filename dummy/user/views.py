from django.shortcuts import render
from user.forms import LoginForm
from user.forms import SignupForm
from django.contrib.auth import hashers
from django.contrib import messages


def user_home(request):
    
    return render(request,'user/home.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get['password']
            hashed_password = make_password(password)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/user_login.html',{'form':form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            password = form.cleaned_data.get('password')
            conf_password = form.cleaned_data.get('confirm_password')
            print(password,conf_password)
            if password == conf_password:
                messages.success(request, f'Account created for { username}!')
                return redirect(url 'user_home')
            else:
                messages.error(request, f'passwords mismatch')
    else:
        form = SignupForm()
    return render(request,'user/user_signup.html',{'form':form})

def update_progress(request):
    return render(request,'user/update_progress.html')

def user_account(request):
    return render(request,'user/user_account.html')
