from django.contrib import admin
from django.urls import path, include
from final import views
from final.urls import metal, auth, admin_crud
from django.conf import settings 
from django.conf.urls.static import static

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
    path('sesion/', views.sesion, name='sesion'),
    path('registro/', views.registro, name='registro'),
]
