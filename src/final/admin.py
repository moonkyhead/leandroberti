from django.contrib import admin

# Register your models here.

from.models import Usuario, Musica, Artista

admin.site.register(Musica)
admin.site.register(Artista)
admin.site.register(Usuario)
