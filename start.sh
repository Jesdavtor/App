#!/bin/bash
# Script de inicio para JDApp en Render

echo "Iniciando JDApp..."
echo "Configuración actual:"
echo "DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"
echo "Directorio actual: $(pwd)"
echo "Contenido del directorio:"
ls -la

# Ejecutar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar gunicorn con JDApp
echo "Iniciando gunicorn con JDApp.wsgi:application..."
gunicorn JDApp.wsgi:application --bind 0.0.0.0:$PORT --workers 4 