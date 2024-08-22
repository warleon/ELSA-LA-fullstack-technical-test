from django.contrib import admin
from users.models import (Person,Helper,Adopter)

# Register your models here.

admin.site.register(Person)
admin.site.register(Helper)
admin.site.register(Adopter)