from django.test import TestCase
from django.contrib.auth.models import User
from .models import projectInfo, projectSkills, userProjectInfo
# Create your tests here.

class userProjectTest(TestCase):
	def setUp(self):
		user = User.objects.create_user(
				username = "test@mail.com",
				first_name = "first",
				last_name = "last",
				password = "password",
				email = "test@mail.com"
			)
		project = projectInfo.objects.create(
				project_title = "Test",
				project_description = "Testing project details",
				project_owner = user,
				required_contributors = 3
			)
		
