from rest_framework import serializers
from .models import skillsList

class skillListSerializer(serializers.ModelSerializer):
	class Meta:
		model = skillsList
		fields = '__all__'