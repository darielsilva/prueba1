from django.db import models

# Create your models here.
class Amo(models.Model):

    usuario = models.CharField(max_length = 9)
    contrasena = models.CharField(max_length = 9)
    nombre = models.CharField(max_length = 20)
    email = models.EmailField()
    direccion = models.CharField(max_length = 100)
    comuna = models.CharField(max_length = 30)
    phone = models.CharField(max_length=20)
    encontrado = models.BooleanField()
        
    def __unicode__(self):
        return self.nombre

class Animal(models.Model):

    id_amo = models.ForeignKey('Amo')
    nombre = models.CharField(max_length = 20)
    animal = models.CharField(max_length = 10)
    raza = models.CharField(max_length = 20, null = True, blank = True)
    sexo = models.CharField(max_length = 20, null = True, blank = True)
    codigofoto = models.CharField(max_length = 15)
        
    def __unicode__(self):
        return self.nombre