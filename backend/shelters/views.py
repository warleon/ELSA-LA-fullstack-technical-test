from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from shelters.models import Shelter
from shelters.serializers import ShelterSerializer
from common.genericCRUDView import GenericCRUDView

# Create your views here.
class ShelterCRUDView(GenericCRUDView):
    model = Shelter
    serializer_class = ShelterSerializer 