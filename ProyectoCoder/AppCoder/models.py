from django.db import models

# Create your models here.

class Estudiante(models.Model):

    # no se pone __init__ se ingresan atributos directo

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()
   

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    edad = models.IntegerField() 
    
class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()