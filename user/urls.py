from django.contrib import admin
from django.urls import path,include
from .views import register, checkUserName, isLogin, userLogout, saveUserInfo, fetchUserDetails

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register),
    path('login/', obtain_auth_token),
    path('check_username/', checkUserName),
    path('check_login/', isLogin),
    path('logout/', userLogout),
    path('save_user_info/', saveUserInfo),
    path('get_user_info/', fetchUserDetails)
]
