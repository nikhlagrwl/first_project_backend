from django.urls import path,include
from .views import createProject

urlpatterns = [
	path('create_new_project/', createProject)
]