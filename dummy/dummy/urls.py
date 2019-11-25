from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('author/',include('author.urls')),
    path('book/',include('book.urls')),
]
