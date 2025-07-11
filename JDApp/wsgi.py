"""WSGI config for JDApp project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JDApp.settings')

application = get_wsgi_application()
