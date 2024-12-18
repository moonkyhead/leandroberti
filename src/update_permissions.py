import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Get the user
user = User.objects.get(username='leandro')

# Set permissions
user.is_staff = True
user.is_superuser = True
user.save()

print("Permissions updated successfully!")
