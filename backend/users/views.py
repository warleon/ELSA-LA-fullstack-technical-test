from common.genericCRUDView import GenericCRUDView
from users.models import Person, Helper, Adopter
from users.serializers import PersonSerializer, HelperSerializer, AdopterSerializer

# Create your views here.
class PersonCRUDView(GenericCRUDView):
    model = Person
    serializer_class = PersonSerializer 
class HelperCRUDView(GenericCRUDView):
    model = Helper
    serializer_class = HelperSerializer 
class AdopterCRUDView(GenericCRUDView):
    model = Adopter
    serializer_class = AdopterSerializer 