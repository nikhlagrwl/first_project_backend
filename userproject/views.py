from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser

from .serializer import projectInfoSerializer, projectSkillsSerializer

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

# @csrf_exempt
@api_view(["POST", ])
@permission_classes([IsAuthenticated, ])
def createProject(request):
	if request.method == "POST":
		token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
		username = Token.objects.get(key = token).user.username
		data = JSONParser().parse(request)

		details = data["details"] #details of project except the skill list
		skill_ids = data["skills"] #the skill list for the particular project

		details["project_owner"] = username
		skill_data = []

		response = {}
		status = 200
		project_serializer = projectInfoSerializer(data = details) #saving the project details

		if project_serializer.is_valid():
			project_serializer.save()
			project_id = project_serializer.data["project_id"]

			#only if the project is saved in Db save the skills related to this project
			if project_id is not None:
				for ids in skill_ids:
					temp = {}
					temp["project_id"] = project_id
					temp["skill_id"] = ids
					skill_data.append(temp)

				skill_serializer = projectSkillsSerializer(data = skill_data, many = True) #saving the skills of the project

				if skill_serializer.is_valid():
					skill_serializer.save()
					response["response"] = "project creation success"
				else:
					status = 400
					response["response"] = "Error in saving skills of project"
			else:
				status = 400
				response["response"] = "Error in saving the project"


		else:
			status = 400
			response["response"] = "Invalid data in the project details"

		return JsonResponse(response, status = status)
