from rest_framework import serializers
from .models import projectInfo, projectSkills

class projectInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = projectInfo
		fields = ['project_id', 'project_title', 'project_description', 'project_owner']

class projectSkillsSerializer(serializers.ModelSerializer):
	class Meta:
		model = projectSkills
		fields = '__all__'