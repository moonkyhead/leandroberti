from django.contrib import admin
from .models import Usuario, Banda, Artista

# Register your models here.

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo_electronico', 'usuario')
    search_fields = ('nombre', 'usuario', 'correo_electronico')
    ordering = ('nombre',)
