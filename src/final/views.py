from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Banda, Artista

# Create your views here.

def home(request):
    return render(request, 'final/home.html')

def index(request):
    return render(request, 'final/index.html')

def instructores(request):
    return render(request, 'final/instructores.html')

def numetal(request):
    return render(request, 'final/numetal.html')

def trashmetal(request):
    return render(request, 'final/trashmetal.html')

def deathmetal(request):
    return render(request, 'final/deathmetal.html')

def korn(request):
    return render(request, 'final/korn.html')

def disturbed(request):
    return render(request, 'final/disturbed.html')

def deftones(request):
    return render(request, 'final/deftones.html')

def metallica(request):
    return render(request, 'final/metallica.html')

def megadeth(request):
    return render(request, 'final/megadeth.html')

def testament(request):
    return render(request, 'final/testament.html')

def children(request):
    return render(request, 'final/children.html')

def archenemy(request):
    return render(request, 'final/archenemy.html')

def cannibal(request):
    return render(request, 'final/cannibal.html')

def sesion(request):
    return render(request, 'final/sesion.html')

def registro(request):
    return render(request, 'final/registro.html')

# INDEX
def index(request):
    return render(request, 'final/index.html')

# CRUD Usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'final/listar_usuarios.html', {'usuarios': usuarios})

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo_electronico = request.POST['correo_electronico']
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            usuario=usuario,
            contrasena=contrasena
        )
        messages.success(request, 'Usuario registrado con éxito.')
        return redirect('listar_usuarios')
    return render(request, 'final/registrar_usuario.html')

def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.correo_electronico = request.POST['correo_electronico']
        usuario.usuario = request.POST['usuario']
        usuario.contrasena = request.POST['contrasena']
        usuario.save()
        messages.success(request, 'Usuario actualizado con éxito.')
        return redirect('listar_usuarios')
    return render(request, 'final/actualizar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado con éxito.')
    return redirect('listar_usuarios')

# CRUD Bandas
def crear_banda(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Banda.objects.create(nombre=nombre)
        messages.success(request, 'Banda creada con éxito.')
        return redirect('listar_bandas')
    return render(request, 'final/crear_banda.html')

def listar_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'final/listar_bandas.html', {'bandas': bandas})

def actualizar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        banda.nombre = request.POST['nombre']
        banda.save()
        messages.success(request, 'Banda actualizada con éxito.')
        return redirect('listar_bandas')
    return render(request, 'final/actualizar_banda.html', {'banda': banda})

def eliminar_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    banda.delete()
    messages.success(request, 'Banda eliminada con éxito.')
    return redirect('listar_bandas')

# CRUD Artistas
def crear_artista(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        Artista.objects.create(nombre=nombre)
        messages.success(request, 'Artista creado con éxito.')
        return redirect('listar_artistas')
    return render(request, 'final/crear_artista.html')

def listar_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'final/listar_artistas.html', {'artistas': artistas})

def actualizar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    if request.method == 'POST':
        artista.nombre = request.POST['nombre']
        artista.save()
        messages.success(request, 'Artista actualizado con éxito.')
        return redirect('listar_artistas')
    return render(request, 'final/actualizar_artista.html', {'artista': artista})

def eliminar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    artista.delete()
    messages.success(request, 'Artista eliminado con éxito.')
    return redirect('listar_artistas')

def metal(request):
    return render(request, 'final/metal.html')

def pantera(request):
    return render(request, 'final/pantera.html')