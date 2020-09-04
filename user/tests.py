from django.test import TestCase
from django.contrib.auth.models import User
from .models import userInfo, userSkills
from adminpanel.models import skillsList

# Create your tests here.

class registrationTestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user(username = "abc@email.com", password = "password@123", first_name = "first_name", last_name = "last_name", email = "abc@email.com")
		userInfo.objects.create(username = user, country = "India", state = "West Bengal", contact_no = "1234567899", college_name = "IIT Kharagpur", city = "Kolkata")

	def test_user_data(self):
		user = User.objects.get(username = "abc@email.com")
		self.assertEqual(user.first_name, 'first_name')
		self.assertEqual(user.last_name, 'last_name')
		self.assertEqual(user.email, 'abc@email.com')

	def test_user_info(self):
		user = User.objects.get(username = "abc@email.com")
		userDetails = userInfo.objects.get(username = user)
		self.assertEqual(userDetails.country, 'India')
		self.assertEqual(userDetails.state, 'West Bengal')
		self.assertEqual(userDetails.contact_no, '1234567899')
		self.assertEqual(userDetails.college_name, 'IIT Kharagpur')
		self.assertEqual(userDetails.city, 'Kolkata')
		