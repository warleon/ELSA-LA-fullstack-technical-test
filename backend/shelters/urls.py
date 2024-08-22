from django.urls import path
from shelters.views import ShelterListView

urlpatterns=[
    path('shelters/',ShelterListView.as_view(),name='shelter-list'),
]
