from rest_framework import serializers
from adoptions.models import Adoption

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'