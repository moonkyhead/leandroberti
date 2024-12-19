import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


try:
    admin_user = User.objects.get(username='admin')
except User.DoesNotExist:
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')


admin_user.is_superuser = True
admin_user.is_staff = True
admin_user.save()


all_permissions = Permission.objects.all()
admin_user.user_permissions.add(*all_permissions)

print(f"Fixed permissions for user: {admin_user.username}")
print(f"Is superuser: {admin_user.is_superuser}")
print(f"Is staff: {admin_user.is_staff}")
print(f"Number of permissions: {admin_user.user_permissions.count()}")
