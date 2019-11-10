from django.contrib import admin
from .models import Local, Distrito, Servicio, Categoria, Genero, Cliente, Actor, Horario, Pelicula, Sala, Reserva

# Register your models here.
admin.site.register(Local)
admin.site.register(Distrito)
admin.site.register(Servicio)
admin.site.register(Categoria)
admin.site.register(Genero)
admin.site.register(Cliente)
admin.site.register(Actor)
admin.site.register(Horario)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Reserva)

