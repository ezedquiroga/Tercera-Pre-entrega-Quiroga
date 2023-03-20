from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length=40)
    habitacion = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)


class Huspedes(models.Model):
    nombre = models.CharField(max_length= 40)
    Email = models.CharField(max_length=40)
    telefono = models.IntegerField()


class Cancelacion(models.Model):
    nombre =models.CharField(max_length=40)
