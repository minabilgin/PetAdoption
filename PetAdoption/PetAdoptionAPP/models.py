from django.db import models


# Create your models here.


class Pet(models.Model):
    id = models.IntegerField(max_length=10, null=False)
    sex = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=10)
    age = models.IntegerField(max_length=3, null=False)
    type = models.CharField(max_length=50, null=False)


class PaidPets(models.Model):
    price = models.IntegerField(max_length=10)
    pets = models.OneToOneField(Pet, on_delete=models.CASCADE, null=True)


class PetStuff(models.Model):
    name = models.CharField(max_length=25, null=False)
    price = models.IntegerField(max_length=10, null=False)
    type = models.CharField(max_length=50, null=False)
    image = models.ImageField(null=False)
    description = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=100, null=False)





