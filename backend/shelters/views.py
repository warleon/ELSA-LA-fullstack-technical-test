from rest_framework.generics import ListAPIView

from shelters.models import Shelter
from shelters.serializers import ShelterSerializer
from common.pagination import Paginator

# Create your views here.

class ShelterListView(ListAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    pagination_class = Paginator 
