from django.db import models

from users.models import (Helper,Adopter)
from animals.models import Animal

# Create your models here.

class Adoption(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE)  # helper that helped in the adoption
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE)  # adopter that realizes the adoption
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)  # animal that is being adopted
    adoption_date = models.DateTimeField(auto_now_add=True)  # date when the adoption took place

    def __str__(self):
        return f"Adoption of {self.animal} by {self.adopter} with the help of {self.helper} on {self.adoption_date}"