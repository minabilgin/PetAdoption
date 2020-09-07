from django.contrib import admin
from .models import Pet, PaidPets, PetStuff

# Register your models here.


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["id", "sex", "name", "age", "type"]


@admin.register(PaidPets)
class PaidPetAdmin(admin.ModelAdmin):
    list_display = ["id", "sex", "name", "age", "type", "price"]


@admin.register(PetStuff)
class PetStuffAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "type", "image", "description", "location"]


