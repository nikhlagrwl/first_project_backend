from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# Table for user's additional details
class userInfo(models.Model):
	username = models.OneToOneField(User, primary_key = True, db_column = 'username', on_delete = models.CASCADE)
	country = models.CharField(max_length = 100, db_column = "Country")
	state = models.CharField(max_length = 100, db_column = "State")
	contact_no = models.CharField(max_length = 10, db_column = 'Contact No.')
	gender = models.CharField(max_length = 10, db_column = 'Gender')
	college_name = models.CharField(max_length = 150, db_column = "College Name")
	# college_id = models.IntegerField(db_column = 'College Id', null = True)
	city = models.CharField(max_length = 50, db_column = 'City')

class userSkills(models.Model):
	username = models.CharField(max_length = 150, db_column = "Username")
	skill = models.IntegerField(db_column = "Skill Name")

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
	if created:
		Token.objects.create(user = instance)