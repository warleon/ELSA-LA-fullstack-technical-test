from django.urls import path
from shelters.views import ShelterCRUDView

urlpatterns=[
    path('shelters/',ShelterCRUDView.as_view(),name='shelter-CRUD'),
]
