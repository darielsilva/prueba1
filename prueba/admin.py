from django.contrib import admin
from .models import Amo,Animal

@admin.register(Amo)
class AmoAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'contrasena', 'nombre', 'email', 'direccion', 'comuna', 'phone', 'encontrado']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
	list_display = ['id_amo', 'nombre', 'animal', 'raza', 'sexo', 'codigofoto']