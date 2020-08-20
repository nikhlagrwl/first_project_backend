from django.urls import path,include
from .views import getSkills

urlpatterns = [
	path('get_skill_list/', getSkills)
]