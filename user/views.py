from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from user.serializer import UserSerializer



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
		status = 0
		try:
			print("trying ------------")
			user = User.objects.get(username = username)
			user_data['response'] = 'Username already exists'
			status = 400
		except ObjectDoesNotExist :
			print("first exception ------------")
			user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email )
			user.save()
			token = Token.objects.get(user = user).key
			user_data['username'] = username
			user_data['token'] = token
			user_data['response'] = 'registration successfull'
			status = 200
			# return JsonResponse(user_data, status = 201)
		except:
			print("Second exception ------------")
			user_data['response'] = 'registration failed'
			status = 400
		return JsonResponse(user_data, status = status)


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
			return HttpResponse(user_data, status = 201)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def is_login(request):
	if request.method == "GET":
		print("user is authenticated")
		token = JSONParser().parse(request)['token']
		user = Token.objects.get(key = token).user
		data = {}
		if user is not None:
			login(request, user)
			data['first_name'] = user.first_name
			data['last_name'] = user.last_name
			data['email'] = user.email
			data['response'] = 'authentication successfull'
			return JsonResponse(data, status = 200)
		else:
			data['response'] = 'authentication unsuccessfull'
			return HttpResponse(data, status = 400)

def user_logout(request):
	if request.method == "GET":
		logout(request)
		data = {}
		data['response'] = 'logout success'
		return JsonResponse(data, status = 201)


