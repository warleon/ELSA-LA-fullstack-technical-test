from rest_framework import serializers

from users.models import Person, Adopter, Helper

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = '__all__'
class HelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helper
        fields = '__all__'