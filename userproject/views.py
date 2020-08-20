from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from .models import projectInfo
from .serializer import projectInfoSerializer

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.

# @csrf_exempt
@api_view(["POST", ])
@permission_classes([IsAuthenticated, ])
def createProject(request):
	if request.method == "POST":
		token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
		username = Token.objects.get(key = token).user.username
		data = JSONParser().parse(request)
		data["project_owner"] = username

		response = {}
		status = 200
		serializer = projectInfoSerializer(data = data)

		if serializer.is_valid():
			serializer.save()
			response["response"] = "project creation success"

		else:
			response["response"] = "unseccessful"
			status = 400

		return JsonResponse(response, status = status)