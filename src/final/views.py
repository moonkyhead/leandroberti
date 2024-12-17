from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.



def home(request):
    return render(request, 'final/home.html')

def sesion(request):
    return render(request, 'final/sesion.html')

def registro(request):
    return render(request, 'final/registro.html')

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


