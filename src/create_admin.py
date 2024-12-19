import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User


User.objects.filter(username='admin').delete()


user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

print("Superuser created successfully!")
