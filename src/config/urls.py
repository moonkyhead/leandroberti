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
from django.conf import settings # para probar nuevos archivos
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('home/', views.home),
    path('sesion/', views.sesion),
    # path('sesion/registro', views.sesion),
    path('registro/', views.registro),
    path('registro/index/', views.index),
    path('sesion/index/', views.index),
    path('index/', views.index),
    path('index/numetal/', views.numetal),
    path('index/trashmetal/', views.trashmetal),
    path('index/deathmetal/', views.deathmetal),
    path('index/instructores/', views.instructores),
    path('index/numetal/korn/', views.korn),
    path('index/numetal/disturbed/', views.disturbed),
    path('index/numetal/deftones/', views.deftones),
    path('index/trashmetal/metallica/', views.metallica),
    path('index/trashmetal/megadeth/', views.megadeth),
    path('index/trashmetal/testament/', views.testament),
    path('index/deathmetal/archenemy/', views.archenemy),
    path('index/deathmetal/children/', views.children),
    path('index/deathmetal/cannibal/', views.cannibal),
    path('sesion/index/', views.index),
    path('sesion/index/numetal/', views.numetal),
    path('sesion/index/trashmetal/', views.trashmetal),
    path('sesion/index/deathmetal/', views.deathmetal),
    path('sesion/index/numetal/korn/', views.korn),
    path('sesion/index/numetal/disturbed/', views.disturbed),
    path('sesion/index/numetal/deftones/', views.deftones),
    path('sesion/index/trashmetal/metallica/', views.metallica),
    path('sesion/index/trashmetal/megadeth/', views.megadeth),
    path('sesion/index/trashmetal/testament/', views.testament),
    path('sesion/index/deathmetal/archenemy/', views.archenemy),
    path('sesion/index/deathmetal/children/', views.children),
    path('sesion/index/deathmetal/cannibal/', views.cannibal),
    path('registro/index/numetal/', views.numetal),
    path('registro/index/trashmetal/', views.trashmetal),
    path('registro/index/deathmetal/', views.deathmetal),
    path('registro/index/numetal/korn/', views.korn),
    path('registro/index/numetal/disturbed/', views.disturbed),
    path('registro/index/numetal/deftones/', views.deftones),
    path('registro/index/trashmetal/metallica/', views.metallica),
    path('registro/index/trashmetal/megadeth/', views.megadeth),
    path('registro/index/trashmetal/testament/', views.testament),
    path('registro/index/deathmetal/archenemy/', views.archenemy),
    path('registro/index/deathmetal/children/', views.children),
    path('registro/index/deathmetal/cannibal/', views.cannibal),
]
