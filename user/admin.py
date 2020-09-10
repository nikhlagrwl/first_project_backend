from django.contrib import admin
from user.models import userInfo, userSkills


# Register your models here.

#admin panel for user info table
class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['username', 'contact_no', 'gender', 'country', 'state', 'city', 'college_name']

admin.site.register(userInfo, UserInfoAdmin)

#admin panel for user skills table
class userSkillsAdmin(admin.ModelAdmin):
	list_display = ['username', 'skill']

admin.site.register(userSkills, userSkillsAdmin)
