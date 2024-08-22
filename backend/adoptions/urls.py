from django.urls import path
from adoptions.views import AdoptionCRUDView

urlpatterns = [
    path('adoptions/', AdoptionCRUDView.as_view(), name='adoption-CRUD'),
]