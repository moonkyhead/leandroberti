import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from final.models import Usuario, Banda, Artista

def create_superuser():
    User.objects.filter(is_superuser=True).delete()
    
    
    superuser = User.objects.create_superuser(
        username='superadmin',
        email='superadmin@example.com',
        password='superadmin123'
    )
    
  
    usuario_content_type = ContentType.objects.get_for_model(Usuario)
    banda_content_type = ContentType.objects.get_for_model(Banda)
    artista_content_type = ContentType.objects.get_for_model(Artista)
    
   
    for action in ['add', 'change', 'delete', 'view']:
        for content_type in [usuario_content_type, banda_content_type, artista_content_type]:
            codename = f'{action}_{content_type.model}'
            Permission.objects.get_or_create(
                codename=codename,
                name=f'Can {action} {content_type.model}',
                content_type=content_type,
            )
    
 
    all_permissions = Permission.objects.all()
    superuser.user_permissions.add(*all_permissions)
    
    print(f"Superuser created successfully!")
    print(f"Username: superadmin")
    print(f"Password: superadmin123")
    print(f"Is superuser: {superuser.is_superuser}")
    print(f"Is staff: {superuser.is_staff}")
    print(f"Number of permissions: {superuser.user_permissions.count()}")

if __name__ == '__main__':
    create_superuser()
