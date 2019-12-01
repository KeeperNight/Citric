from django.shortcuts import render


def home(request):
    return render(request, 'user/main_home.html')

