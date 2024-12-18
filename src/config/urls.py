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
from django.urls import path, include
from final import views
from final.urls import metal, auth, admin_crud
from django.conf import settings 
from django.conf.urls.static import static



base_patterns = [
    path('', views.index, name='index'),
    path('numetal/', views.numetal, name='numetal'),
    path('trashmetal/', views.trashmetal, name='trashmetal'),
    path('deathmetal/', views.deathmetal, name='deathmetal'),
    path('instructores/', views.instructores, name='instructores'),

    path('numetal/korn/', views.korn, name='korn'),
    path('numetal/disturbed/', views.disturbed, name='disturbed'),
    path('numetal/deftones/', views.deftones, name='deftones'),

    path('trashmetal/metallica/', views.metallica, name='metallica'),
    path('trashmetal/megadeth/', views.megadeth, name='megadeth'),
    path('trashmetal/testament/', views.testament, name='testament'),

    path('deathmetal/archenemy/', views.archenemy, name='archenemy'),
    path('deathmetal/children/', views.children, name='children'),
    path('deathmetal/cannibal/', views.cannibal, name='cannibal'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sesion/', views.sesion, name='sesion'),
    path('registro/', views.registro, name='registro'),


    path('index/', include((base_patterns, 'final'))),
    path('sesion/index/', include((base_patterns, 'final'))),
    path('registro/index/', include((base_patterns, 'final'))),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include(auth.urlpatterns)),  
    path('', include(admin_crud.urlpatterns)),  
    path('index/', views.index, name='index'),
    path('index/', include(metal.urlpatterns)),  
    path('index/instructores/', views.instructores, name='instructores'),
    path('sesion/index/', views.index, name='sesion_index'),
    path('sesion/index/', include(metal.urlpatterns)),
    path('registro/index/', views.index, name='registro_index'),
    path('registro/index/', include(metal.urlpatterns)),
]
