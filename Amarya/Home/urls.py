from django.contrib import admin
from django.urls import path
from Home import views as V

urlpatterns = [
    path('', V.home,name="home"),
    path('signup', V.signup,name="signup"),
    path('signin', V.signin,name="signin"),
    path('signout', V.signout,name="signout"),
]
