from common.genericCRUDView import GenericCRUDView
from shelters.models import Shelter
from shelters.serializers import ShelterSerializer

# Create your views here.
class ShelterCRUDView(GenericCRUDView):
    model = Shelter
    serializer_class = ShelterSerializer 