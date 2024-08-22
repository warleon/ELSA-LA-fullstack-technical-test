from django.contrib import admin
from animals.models import (Specie,Breed,Animal)

# Register your models here.
admin.site.register(Specie)
admin.site.register(Breed)
admin.site.register(Animal)
