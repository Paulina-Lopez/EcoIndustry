from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class InfoImpacto(models.Model):
    pesoTotal = models.PositiveIntegerField(null=False)

class TipoUsuario(models.Model):
    idtipousuario = models.SmallIntegerField(primary_key=True)
    desctipousuario = models.CharField(max_length=20)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombreEmpresa = models.CharField(max_length=45, unique=False, null=False)
    NIT = models.BigIntegerField(null=False)
    correo = models.CharField(max_length=45, null=False)
    clave = models.CharField(max_length=30, null=False, unique=False)
    direccion = models.CharField(max_length=50, null=False, unique=False)
    idtipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

class Bonificacion(models.Model):
    idbonificacion = models.AutoField(primary_key=True, null=False)
    nombre= models.CharField(max_length=30,null=False)
    valor = models.IntegerField(null=False, unique=False)
    imagen = models.CharField(max_length=300,null=False)

class Usuario_Bonificacion(models.Model):
    identificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    idbonificacion = models.ForeignKey(Bonificacion, on_delete=models.CASCADE)

class Puntos_Usuarios(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    identificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    
class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, null=False)
    identificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    desComent= models.CharField(max_length=300, null=False)
    
class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, primary_key=True, null=False)
    nombreConductor = models.CharField(max_length=45, unique=False, null=False)
    capacidad = models.CharField(max_length=45, unique=False, null=False)
    disponibilidad = models.CharField(max_length=45, unique=False, null=False)
    
class Agenda(models.Model):
    idAgenda = models.AutoField(primary_key=True, null=False)
    fechaAgenda = models.DateField(null=False)
    estado = models.CharField(max_length=30, null=False)
    identificacion = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10, null=False)


