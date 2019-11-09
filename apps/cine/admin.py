from django.contrib import admin
from .models import Local, Distrito, Servicio

# Register your models here.
admin.site.register(Local)
admin.site.register(Distrito)
admin.site.register(Servicio)