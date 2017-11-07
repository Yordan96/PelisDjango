from django.db import models
from django.contrib import admin
# Create your models here.



class Pelicula(models.Model):
    titulo  =   models.CharField(max_length=30)
    idioma= models.CharField(max_length=15)
    genero= models.CharField(max_length=15)
    duracion= models.CharField(max_length=15)
    anio= models.IntegerField(max_length=4)
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre  =   models.CharField(max_length=30)
    telefono= models.CharField(max_length=15)
    DPI= models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    peliculas   = models.ManyToManyField(Pelicula, through='Alquiler')
    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    actor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class AlquilerInLine(admin.TabularInline):
    model = Alquiler
    extra = 1

class PeliculaAdmin(admin.ModelAdmin):
    inlines = (AlquilerInLine,)

class UsuarioAdmin (admin.ModelAdmin):
    inlines = (AlquilerInLine,)
