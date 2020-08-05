from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.register),
    path('login/', obtain_auth_token),
    path('checkusername/', views.check_user_name),
    path('checklogin/', views.is_login),
    path('logout/', views.user_logout),
]
