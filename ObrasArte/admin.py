from django.contrib import admin
from .models import Artista, ArtistaAdmin, Pintura, PinturaAdmin
# Register your models here.
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Pintura, PinturaAdmin)
