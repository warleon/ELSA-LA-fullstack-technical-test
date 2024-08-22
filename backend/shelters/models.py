from django.db import models

# Create your models here.

class Shelter(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    title = models.CharField(max_length=20)  # title of the shelter
    address = models.CharField(max_length=100)  # address where the shelter is located

    def __str__(self):
        return f"{self.title} - {self.address}"