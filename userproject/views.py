from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from .serializer import projectInfoSerializer, projectSkillsSerializer
from .models import projectInfo, projectSkills

from adminpanel.models import skillsList

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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
			project_owner = user
		) #saving the project details

		if project is not None:
			project.save()
			project_id = project.project_id

			#only if the project is saved in Db save the skills related to this project
			if project_id is not None:
				for ids in skill_ids:
					# temp["project_id"] = project
					skill = skillsList.objects.get(skill_id = ids)

					project_skill = projectSkills.objects.create(project_id = project, skill_id = skill)
					# skill_data.append(temp)

				# print(skill_data)

				# skill_serializer = projectSkillsSerializer(data = skill_data, many = True) #saving the skills of the project

				# if skill_serializer.is_valid():
					# skill_serializer.save()
				response["response"] = "project creation success"
				# else:
				# 	status = 400
				# 	response["response"] = "Error in saving skills of project"
			else:
				status = 400
				response["response"] = "Error in saving the project"


		else:
			status = 400
			response["response"] = "Invalid data in the project details"

		return JsonResponse(response, status = status)
