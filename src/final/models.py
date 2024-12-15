from django.db import models

# Create your models here.

from django.db import models

class Nombre(models.Model):
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor


class Apellido(models.Model):
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    usuario = models.CharField(max_length=15, unique=True)
    contrasena = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario


from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['firstName']
        apellido = request.POST['lastName']
        correo_electronico = request.POST['email']
        usuario = request.POST['username']
        contrasena = request.POST['password']

        if Usuario.objects.filter(usuario=usuario).exists() or Usuario.objects.filter(correo_electronico=correo_electronico).exists():
            messages.error(request, 'El usuario o correo ya está registrado.')
            return redirect('registro')

        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            usuario=usuario,
            contrasena=contrasena
        )
        nuevo_usuario.save()
        messages.success(request, 'Registro completado con éxito.')
        return redirect('inicio')

    return render(request, 'registro.html')
