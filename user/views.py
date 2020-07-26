from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from user.models import User
from user.serializer import UserSerializer
# Create your views here.

@csrf_exempt
def user_get_post(request):
	if request.method == 'GET':
		data = User.objects.all()
		serializer = UserSerializer(data, many = True)
		return JsonResponse(serializer.data, safe = False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UserSerializer(data)
		if(serializer.is_valid()):
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
		return HttpResponse(serializer.error, status = 400)
