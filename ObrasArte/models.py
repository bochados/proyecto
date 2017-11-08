from django.db import models
from django.contrib import admin
from django.utils import timezone


class Pintura(models.Model):
    nombre_pintura= models.CharField(max_length=30,default='pinturaa')
    estilo = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre_pintura

class Artista(models.Model):

    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    pinturas = models.ManyToManyField(Pintura, through='Obra')
    def __str__(self):
        return self.nombre


class Obra(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    pintura = models.ForeignKey(Pintura, on_delete=models.CASCADE)

class ObraInline(admin.TabularInline):
    model = Obra
    extra = 1

class ArtistaAdmin(admin.ModelAdmin):
    inlines = (ObraInline,)

class PinturaAdmin(admin.ModelAdmin):
    inlines = (ObraInline,)
# Create your models here.
