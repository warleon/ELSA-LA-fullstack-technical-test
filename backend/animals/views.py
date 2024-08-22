from rest_framework.generics import ListAPIView

from animals.models import Animal,Specie,Breed
from animals.serializers import AnimalSerializer, SpecieSerializer, BreedSerializer
from common.genericCRUDView import GenericCRUDView
# Create your views here.
class SpecieCRUDView(GenericCRUDView):
    model = Specie
    serializer_class = SpecieSerializer
class BreedCRUDView(GenericCRUDView):
    model = Breed
    serializer_class = BreedSerializer
class AnimalCRUDView(GenericCRUDView):
    model = Animal
    serializer_class = AnimalSerializer
