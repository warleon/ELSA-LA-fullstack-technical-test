from django.db import models
from shelters.models import Shelter

# Create your models here.

class Specie(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    title = models.CharField(max_length=10)  # title of the specie e.g. dog or cat

    def __str__(self):
        return self.title

class Breed(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)  # link to the specie that this breed belongs to
    title = models.CharField(max_length=40)  # title of the breed

    def __str__(self):
        return f"{self.title} ({self.specie})"

class Animal(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    name = models.CharField(max_length=15)  # name of the animal
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)  # link to the breed that this animal belongs to
    inscription_date = models.DateTimeField(auto_now_add=True)  # timestamp of the animal's inscription date into the system
    age_at_inscription = models.IntegerField()  # the approximate age of the animal when it was inscribed in the system
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)  # shelter where the animal belongs

    def _str_(self):
        return f"{self.name} ({self.breed})"