from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from user.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

@csrf_exempt
def register(request):
	if request.method == 'GET':
		data = User.objects.all()
		serializer = UserSerializer(data, many = True)
		return JsonResponse(serializer.data, safe = False)

	if request.method == "POST":
		data = JSONParser().parse(request)

		username = data['username']
		password = data['password']
		first_name = data['first_name']
		last_name = data['last_name']
		email = data['email']

		user_data = {}

		try:
			user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email )
			user.save()
			user_data['username'] = username
			user_data['response'] = 'registration successfull'
			return JsonResponse(user_data, status = 201)
		except:
			user_data['response'] = 'registration failed'
			return JsonResponse(user_data, status = 400)

@csrf_exempt
def user_login(request):
	if request.method == "POST":
		recieved_data = JSONParser().parse(request)
		username = recieved_data['username']
		password = recieved_data['password']
		data = {}
		user = User.objects.get(username = username)
		if user is not None:
			print("Username valid")
			print(password)
			print(user.password)
			if check_password(password, user.password):
				print("password valid")
				login(request, user)
				data['response'] = 'login successfull'
				data['username'] =  username
				token = Token.objects.get(user = user).key
				data['token'] = token
				return JsonResponse(data, status = 201)
			else:
				print("password Invalid")
				data['response'] = 'invalid password'
				return JsonResponse(data, status = 400)
		else:
			print("Username Invalid")
			data['response'] = 'invalid username'
			return JsonResponse(data, status = 400)

@csrf_exempt
def check_user_name(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		username = data['username']
		print("username printing ----------------")
		print(username)
		print("----------------")

		user_data = {}
		try:
			user = User.objects.get(username = username)
			print(user)
			user_data['response'] = 'username not available'

			return HttpResponse(user_data, status = 400)
		except:
			user_data['response'] = 'username available'
			return HttpResponse(user_data, status = 201);

# def find_user(request):


# @csrf_exempt
# def user_get_post(request):
# 	if request.method == 'GET':
# 		data = User.objects.all()
# 		serializer = UserSerializer(data, many = True)
# 		return JsonResponse(serializer.data, safe = False)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = UserSerializer(data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status = 201)
# 		return HttpResponse(serializer.error, status = 400)
