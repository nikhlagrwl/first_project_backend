from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
# Create your views here.

@csrf_exempt
def register(request):
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
			if check_password(password, user.password):
				login(request, user)

				data['response'] = 'login successfull'
				data['username'] =  username
				token = Token.objects.get(user = user).key
				data['token'] = token

				return JsonResponse(data, status = 201)
			else:
				data['response'] = 'invalid password'
				return HttpResponse(data, status = 400)
		else:
			data['response'] = 'invalid username'
			return HttpResponse(data, status = 400)

@csrf_exempt
def check_user_name(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		username = data['username']

		user_data = {}
		try:
			user = User.objects.get(username = username)
			user_data['response'] = 'username not available'
			return HttpResponse(user_data, status = 400)
		except:
			user_data['response'] = 'username available'
			return HttpResponse(user_data, status = 201);
@csrf_exempt
def is_login(request):
	if request.method == "POST":
		token = JSONParser().parse(request)['token']
		user = Token.objects.get(key = token).user
		data = {}
		if user is not None:
			username = user.username
			login(request, user)
			data['username'] = username
			data['response'] = 'login successfull'
			return JsonResponse(data, status = 200)
		else:
			data['response'] = 'not logged in'
			return HttpResponse(data, status = 400)





		# print(request.COOKIES)
		# print(request.user);
		# key = 'username'
		# data = {}

		# print("printing is_login ------------------- ")
		# print(request)
		# print(request.session)
		# # print(username)
		# print("---------------------")

		# if key in request.session:
		# 	data['username'] = "username"
		# 	data['response'] = 'logged in'
		# 	return JsonResponse(data, status = 201)
		# else:
		# 	data['response'] = 'not logged in'
		# 	return JsonResponse(data, status = 400)


def user_logout(request):
	if request.method == "GET":
		logout(request)
		data = {}
		data['response'] = 'logout success'
		return HttpResponse(data, status = 201)
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
