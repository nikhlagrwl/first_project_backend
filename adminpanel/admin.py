from django.contrib import admin
from adminpanel.models import collegeList, skillsList

# Register your models here.

#admin panel for college list table
class CollegeListAdmin(admin.ModelAdmin):
	list_display = ['college_id', 'college_name', 'college_city']

admin.site.register(collegeList, CollegeListAdmin)

#admin panel for skills list table
class skillsListAdmin(admin.ModelAdmin):
	list_display = ['skill_id', 'skill_name']

admin.site.register(skillsList, skillsListAdmin)