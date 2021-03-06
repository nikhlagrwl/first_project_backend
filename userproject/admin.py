from django.contrib import admin
from userproject.models import projectInfo, projectSkills, userProjectInfo
# Register your models here.


#admin panel for projectInfo Table
class projectInfoAdmin(admin.ModelAdmin):
	list_display = ['project_id', 'project_title', 'project_description', 'created_at', 'project_owner', 'start_date', 'end_date', 'required_contributors']

admin.site.register(projectInfo, projectInfoAdmin)

#admin panel for projectSkills table
class projectSkillsAdmin(admin.ModelAdmin):
	list_display = ['id', 'project_id', 'skill_id', 'status']

admin.site.register(projectSkills, projectSkillsAdmin)


#admin panel for userProjectInfo Table
class userProjectInfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'project', 'user_status']

admin.site.register(userProjectInfo, userProjectInfoAdmin)
