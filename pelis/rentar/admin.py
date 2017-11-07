from django.contrib import admin
from rentar.models import Pelicula, PeliculaAdmin, Usuario, UsuarioAdmin

# Register your models here.
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
