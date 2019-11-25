from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('about/',views.about_user,name="user"),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.user_signup,name='user_signup'),
    path('update_progress/',views.update_progress,name='update_progress'),
]
