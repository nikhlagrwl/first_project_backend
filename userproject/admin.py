from django.contrib import admin
from userproject.models import projectInfo, projectSkills, userProjectInfo
# Register your models here.


#admin panel for projectInfo Table
class projectInfoAdmin(admin.ModelAdmin):
	list_display = ['project_id', 'project_title', 'project_description', 'created_at', 'project_owner']

admin.site.register(projectInfo, projectInfoAdmin)

#admin panel for projectSkills table
class projectSkillsAdmin(admin.ModelAdmin):
	list_display = ['project_id', 'skill_id']

admin.site.register(projectSkills, projectSkillsAdmin)


#admin panel for userProjectInfo Table
class userProjectInfoAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'user_status']

admin.site.register(userProjectInfo, userProjectInfoAdmin)
