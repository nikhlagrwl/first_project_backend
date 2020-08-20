from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .serializer import skillListSerializer
from .models import skillsList

from django.http import JsonResponse
# Create your views here.


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def getSkills(request):
	queryset = skillsList.objects.all()
	serializer = skillListSerializer(skillsList.objects.all(), many = True)
	return JsonResponse(serializer.data, status = 200, safe = False)