from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from common.pagination import Paginator

class GenericCRUDView(APIView):
    permission_classes = [IsAuthenticated]
    model = None  # The model to operate on
    serializer_class = None  # The serializer to use

    def get(self, request, *args, **kwargs):
        generic_id = request.query_params.get('id', None)
        if generic_id: # Fetch a single object by ID
            generic = get_object_or_404(self.model, id=generic_id)
            serializer = self.serializer_class(generic)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: # Fetch a paginated list of objects
            generics = self.model.objects.all()
            paginator = Paginator()  
            paginated_generics = paginator.paginate_queryset(generics, request)
            serializer = self.serializer_class(paginated_generics, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        generic_id = request.query_params.get('id', None)
        if not generic_id:
            return Response({"detail": "ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
        generic = get_object_or_404(self.model, id=generic_id)
        serializer = self.serializer_class(generic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        generic_id = request.query_params.get('id', None)
        if not generic_id:
            return Response({"detail": "ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        generic = get_object_or_404(self.model, id=generic_id)
        generic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)