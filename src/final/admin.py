from django.contrib import admin

# Register your models here.

from.models import Usuario, Banda, Artista

admin.site.register(Banda)
admin.site.register(Artista)
admin.site.register(Usuario)


@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    List_display = ('nombre', 'genero',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    List_display = ('nombre', 'genero',)
    search_fields = ('nombre',)
    ordering = ('nombre',)



@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    List_display = ('nombre', 'apellido', 'correo electronico', 'usuario',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
