from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.register),
    path('login/', views.user_login),
    path('checkusername/', views.check_user_name),
]
