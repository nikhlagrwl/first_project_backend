from django.test import TestCase
from django.contrib.auth.models import User
from .models import projectInfo, projectSkills, userProjectInfo
from adminpanel.models import skillsList
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
		skills = [1, 2, 3, 4]
		# data = []
		for ids in skills:
			print(ids)
			skill = skillsList.objects.get(skill_id = ids)
		# 	temp = projectSkills(project_id = project, skill_id = skill)
		# 	data.append(temp)
		# projectSkills.objects.bulk_create(data)

	def test_project_status(self):
		project = projectInfo.objects.get(project_title = "Test")
		user = User.objects.get(username = "test@mail.com")
		self.assertEqual(project.project_description, "Testing project details")
