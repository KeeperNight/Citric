from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='main_home'),
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('author/',include('author.urls')),
    path('book/',include('book.urls')),
]
