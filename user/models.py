from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# class User_data(models.Model):
# 	first_name = models.CharField(max_length = 100)
# 	last_name = models.CharField(max_length = 100)
# 	email = models.EmailField(unique = True)
# 	contact_no = models.CharField(max_length = 100)
class UserInfo(models.Model):
	username = models.CharField(max_length = 100, primary_key = True)
	contact_no = models.CharField(max_length = 10)
	gender = models.CharField(max_length = 10)
	age = models.CharField(max_length = 2)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
	if created:
		Token.objects.create(user = instance)