from django.db import models

# Create your models here.


class Personas(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    DNI=models.CharField(max_length=9, unique=True)
    fecha_nacimiento=models.DateField()
    GBA=models.BooleanField()