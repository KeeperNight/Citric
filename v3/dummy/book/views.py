from django.shortcuts import render

from django.http import HttpResponse


def about_book(request):
    return HttpResponse("<h1>Book dummy page</h1>")


