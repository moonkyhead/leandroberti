import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing user if it exists
User.objects.filter(username='admin').delete()

# Create a new superuser
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

print("Superuser created successfully!")
