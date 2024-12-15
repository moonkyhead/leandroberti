"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from final import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('index/', views.index),
    path('index/numetal/', views.numetal),
    path('index/trashmetal/', views.trashmetal),
    path('index/deathmetal/', views.deathmetal),
    path('index/numetal/korn/', views.korn),
    path('index/numetal/disturbed/', views.disturbed),
    path('index/numetal/deftones/', views.deftones),
    path('index/trashmetal/metallica/', views.metallica),
    path('index/trashmetal/megadeth/', views.megadeth),
    path('index/trashmetal/testament/', views.testament),
    path('index/deathmetal/archenemy/', views.archenemy),
    path('index/deathmetal/children/', views.children),
    path('index/deathmetal/cannibal/', views.cannibal),
    path('home/sesion/', views.sesion),
    path('home/sesion/final', views.sesion),
    path('home/registro/', views.registro),
    path('home/registro/final', views.registro),
    
  
    
]
