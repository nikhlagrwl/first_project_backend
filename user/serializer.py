from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import userInfo


class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class userInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = userInfo
		fields = ['username', 'contact_no', 'gender', 'college_id', 'city', 'country', 'state', 'college_name']
