from django.urls import path,include
from .views import createProject, updateProject, getOwnerProjects, applyOnProject, getAppliedProjects

urlpatterns = [
	path('create_new_project/', createProject),
	path('update_project/', updateProject),
	path('get_owner_project/', getOwnerProjects),
	path('get_applied_projects/', getAppliedProjects),
	path('apply_on_project/', applyOnProject)
]