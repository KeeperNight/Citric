from django.urls import path

from . import views

urlpatterns=[
    path('home/',views.user_home,name="user_home"),
    path('account/',views.user_account,name='user_account'),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.user_signup,name='user_signup'),
    path('update_progress/',views.update_progress,name='update_progress'),
]
