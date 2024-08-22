from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from shelters.models import Shelter
from shelters.serializers import ShelterSerializer
from common.pagination import Paginator

# Create your views here.
class ShelterCRUDView(APIView):
    def get(self, request, *args, **kwargs):
        shelter_id = request.query_params.get('id', None)
        if shelter_id: # Fetch a single shelter by ID
            shelter = get_object_or_404(Shelter, id=shelter_id)
            serializer = ShelterSerializer(shelter)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: # Fetch a paginated list of shelters
            shelters = Shelter.objects.all()
            paginator = Paginator()  
            paginated_shelters = paginator.paginate_queryset(shelters, request)
            serializer = ShelterSerializer(paginated_shelters, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ShelterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        shelter_id = request.query_params.get('id', None)
        if not shelter_id:
            return Response({"detail": "ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
        shelter = get_object_or_404(Shelter, id=shelter_id)
        serializer = ShelterSerializer(shelter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        shelter_id = request.query_params.get('id', None)
        if not shelter_id:
            return Response({"detail": "ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        shelter = get_object_or_404(Shelter, id=shelter_id)
        shelter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)