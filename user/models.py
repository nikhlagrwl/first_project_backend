from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# Table for user's additional details
class userInfo(models.Model):
	username = models.CharField(max_length = 150, primary_key = True, db_column = 'Username')
	contact_no = models.CharField(max_length = 10, db_column = 'Contact No.')
	gender = models.CharField(max_length = 10, db_column = 'Gender')
	college_id = models.IntegerField(db_column = 'College Id', default = None)
	city = models.CharField(max_length = 50, db_column = 'City', default = None)

class userSkills(models.Model):
	username = models.CharField(max_length = 150, db_column = "Username")
	skill = models.IntegerField(db_column = "Skill Name")

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
	if created:
		Token.objects.create(user = instance)