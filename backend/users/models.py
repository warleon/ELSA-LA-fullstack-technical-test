from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    first_name = models.CharField(max_length=15)  # first name of the person
    last_name = models.CharField(max_length=15)  # last name of the person
    email = models.EmailField(max_length=50)  # email of the person
    inscription_date = models.DateTimeField(auto_now_add=True)  # timestamp of the person's inscription date into the system

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Helper(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    info = models.OneToOneField(Person, on_delete=models.CASCADE)  # link to a person's information

    def __str__(self):
        return f"Helper: {self.info}"

class Adopter(models.Model):
    id = models.AutoField(primary_key=True)  # autoincremental id
    person = models.OneToOneField(Person, on_delete=models.CASCADE)  # link to a person's information

    def __str__(self):
        return f"Adopter: {self.person}"