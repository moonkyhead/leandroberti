from django.urls import path
from final import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Usuario CRUD paths
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('actualizar_usuario/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Banda CRUD paths
    path('crear_banda/', views.crear_banda, name='crear_banda'),
    path('listar_bandas/', views.listar_bandas, name='listar_bandas'),
    path('actualizar_banda/<int:banda_id>/', views.actualizar_banda, name='actualizar_banda'),
    path('eliminar_banda/<int:banda_id>/', views.eliminar_banda, name='eliminar_banda'),

    # Artista CRUD paths
    path('crear_artista/', views.crear_artista, name='crear_artista'),
    path('listar_artistas/', views.listar_artistas, name='listar_artistas'),
    path('actualizar_artista/<int:artista_id>/', views.actualizar_artista, name='actualizar_artista'),
    path('eliminar_artista/<int:artista_id>/', views.eliminar_artista, name='eliminar_artista'),
]
