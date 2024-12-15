from django.contrib import admin

# Register your models here.

from.models import Nombre, Apellido, Usuario

admin.site.register(Nombre)
admin.site.register(Apellido)
admin.site.register(Usuario)
