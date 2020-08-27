from django.contrib import admin
from django.urls import path,include
from .views import register, checkUserName, isLogin, userLogout, saveUserInfo, fetchUserDetails

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register),
    path('login/', obtain_auth_token),
    path('checkusername/', checkUserName),
    path('checklogin/', isLogin),
    path('logout/', userLogout),
    path('userinfo/', saveUserInfo),
    path('getUserInfo/', fetchUserDetails)
]
