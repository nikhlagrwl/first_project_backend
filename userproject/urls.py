from django.contrib import admin
from django.urls import path,include
from userproject.views import createProject

urlpatterns = [
	path('create_new_project/', createProject)
]