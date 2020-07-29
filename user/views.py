from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user.serializer import UserSerializer
# Create your views here.

@csrf_exempt
def register(request):
	if request.method == 'GET':
		data = User.objects.all()
		serializer = UserSerializer(data, many = True)
		return JsonResponse(serializer.data, safe = False)
	if request.method == "POST":
		data = JSONParser().parse(request)
		serializer = UserSerializer(data = data)
		if serializer.is_valid():
			account = serializer.save()
			print("---------------------")
			print(type(account))
			print(account)
			print("---------------------")
			return JsonResponse(serializer.data, status = 201)
		return HttpResponse(serializer.error, status = 400)


def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username = username, password = password)
	data = {}
	if user is not None:
		login(request, user)
		data['response'] = 'login successfull'
		data['username'] =  username
		user_data = User.objects.get(username = username)
		token = Token.objects.get(user = user_data).key
		data['token'] = token
	else:
		data['response'] = 'login failed'
	return Response(data)

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
