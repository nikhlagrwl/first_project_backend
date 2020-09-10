from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from .serializer import projectInfoSerializer, projectSkillsSerializer
from .models import projectInfo, projectSkills, userProjectInfo

from adminpanel.models import skillsList

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

# @csrf_exempt
@api_view(["POST", ])
@permission_classes([IsAuthenticated, ])
def createProject(request):
	if request.method == "POST":
		token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
		user = Token.objects.get(key = token).user
		data = JSONParser().parse(request)

		details = data["details"] #details of project except the skill list
		skill_ids = data["skills"] #the skill list for the particular project

		details["project_owner"] = user
		skill_data = []

		print(details)

		response = {}
		status = 200
		project = projectInfo.objects.create(
			project_title = details["project_title"],
			project_description = details["project_description"],
			project_owner = user,
			required_contributors = details["required_contributors"]
		) #saving the project details

		if project is not None:
			project.save()
			project_id = project.project_id

			#only if the project is saved in Db, save the skills related to this project
			if project_id is not None:
				for ids in skill_ids:
					skill = skillsList.objects.get(skill_id = ids)
					project_skill = projectSkills.objects.create(project_id = project, skill_id = skill)
				response["response"] = "project creation success"
			else:
				status = 400
				response["response"] = "Error in saving the project"
		else:
			status = 400
			response["response"] = "Invalid data in the project details"

		return JsonResponse(response, status = status)

@api_view(["POST", ])
@permission_classes([IsAuthenticated, ])
def updateProject(request):
	data = JSONParser().parse(request)
	project_id = data["project_id"]
	project = projectInfo.objects.get(project_id = project_id)

	skill_ids = data["skills"]

	fields = projectSkills.objects.filter(project_id = project)
	for obj in fields:
		obj.status = False
	projectSkills.objects.bulk_update(fields, ['status'])
	for ids in skill_ids:
		skill = skillsList.objects.get(skill_id = ids)
		project_skill = projectSkills.objects.update_or_create(project_id = project, skill_id = skill, defaults = {'status': "1"})

	return JsonResponse({"Response": "Success"}, status = 201)

@api_view(["GET", ])
@permission_classes([IsAuthenticated, ])
def getOwnerProjects(request):
	token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
	user = Token.objects.get(key = token).user

	projects = projectInfo.objects.filter(project_owner = user)

	response = {}
	if projects is None:
		response["data"] = []
	else:
		data = []
		for obj in projects:
			data.append(model_to_dict(obj))
		response["data"] = data
		print(response)

	return JsonResponse(response, status = 201)


@api_view(["GET", ])
@permission_classes([IsAuthenticated, ])
def getAppliedProjects(request):
	token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
	user = Token.objects.get(key = token).user

	projects = userProjectInfo.objects.filter(user = user)

	response = {}
	if projects is None:
		response["data"] = []
	else:
		data = []
		for obj in projects:
			data.append(model_to_dict(obj.project))
		response["data"] = data
		print(response)

	return JsonResponse(response, status = 201)


@api_view(["POST", ])
@permission_classes([IsAuthenticated, ])
def applyOnProject(request):
	token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
	user = Token.objects.get(key = token).user

	data = JSONParser().parse(request)
	project = projectInfo.objects.get(project_id = data["project_id"])

	response = {}
	status = 400
	projectStatus = userProjectInfo.objects.create(
			user = user,
			project = project
		)

	if projectStatus is not None:
		response["response"] = "Success"
		status = 201
	else:
		response["response"] = "Failed"

	return JsonResponse(response, status = status)



