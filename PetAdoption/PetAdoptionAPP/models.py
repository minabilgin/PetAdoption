from django.db import models


# Create your models here.


class Pet(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    sex = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=10)
    age = models.IntegerField(null=False)
    type = models.CharField(max_length=50, null=False)


class PaidPets(models.Model):
    price = models.IntegerField(null=False)
    pets = models.OneToOneField(Pet, on_delete=models.CASCADE, null=True)


class PetStuff(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=25, null=False)
    price = models.IntegerField(null=False)
    type = models.CharField(max_length=50, null=False)
    image = models.ImageField(null=False)
    description = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=100, null=False)





