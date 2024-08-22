from django.urls import path
from users.views import PersonCRUDView, HelperCRUDView, AdopterCRUDView

urlpatterns=[
    path('persons/',PersonCRUDView.as_view(),name='person-CRUD'),
    path('helpers/',HelperCRUDView.as_view(),name='helper-CRUD'),
    path('adopters/',AdopterCRUDView.as_view(),name='adopter-CRUD'),
]
