from rest_framework import serializers
from .models import projectInfo

class projectInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = projectInfo
		fields = ['project_title', 'project_description', 'project_owner']