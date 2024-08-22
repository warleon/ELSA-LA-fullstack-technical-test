from common.genericCRUDView import GenericCRUDView
from adoptions.models import Adoption
from adoptions.serializers import AdoptionSerializer

# Create your views here.

class AdoptionCRUDView(GenericCRUDView):
    model =  Adoption
    serializer_class = AdoptionSerializer
