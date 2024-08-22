from django.urls import path
from animals.views import SpecieCRUDView, BreedCRUDView, AnimalCRUDView

urlpatterns = [
    path('species/', SpecieCRUDView.as_view(), name='specie-CRUD'),
    path('breeds/', BreedCRUDView.as_view(), name='breed-CRUD'),
    path('animals/', AnimalCRUDView.as_view(), name='animal-CRUD'),
]
