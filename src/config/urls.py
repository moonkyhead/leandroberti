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
from final.urls import metal, auth
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include(auth.urlpatterns)),  
    path('index/', views.index, name='index'),
    path('index/', include(metal.urlpatterns)),  
    path('index/instructores/', views.instructores, name='instructores'),
    path('sesion/index/', views.index, name='sesion_index'),
    path('sesion/index/', include(metal.urlpatterns)),
    path('registro/index/', views.index, name='registro_index'),
    path('registro/index/', include(metal.urlpatterns)),
]
