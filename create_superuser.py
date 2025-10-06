import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('Sirojiddin', 'sirojiddin0795@gmail.com', 'messi0795')
    print('Superuser created: username=Sirojiddin, password=messi0795')
else:
    print('Superuser already exists.')
