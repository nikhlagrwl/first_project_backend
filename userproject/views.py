from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from userproject.models import projectInfo

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
		print(data)
		title = data["title"]
		description = data["description"]

		project = projectInfo.objects.create(project_title = title, project_description = description, project_owner = username)
		project.save()

		response = {}
		response["response"] = "project creation success"

		print("project created")

		return JsonResponse(response, status = 200)