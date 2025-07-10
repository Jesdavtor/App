import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fa_ma_api.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="Jtorr").exists():
    User.objects.create_superuser("Jtorr", "jtorr@example.com", "Jestor_123")
    print("Superusuario creado: Jtorr / Jestor_123")
else:
    print("El superusuario ya existe.") 