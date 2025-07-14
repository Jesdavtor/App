@echo off
echo ========================================
echo Iniciando JDApp - Servidor Local
echo ========================================
echo.

echo 1. Activando entorno virtual...
call venv\Scripts\activate.bat

echo.
echo 2. Verificando dependencias...
pip install -r requirements.txt

echo.
echo 3. Ejecutando migraciones...
python manage.py migrate

echo.
echo 4. Recolectando archivos estáticos...
python manage.py collectstatic --noinput

echo.
echo 5. Iniciando servidor de desarrollo...
echo.
echo ========================================
echo Servidor iniciado en: http://127.0.0.1:8000/
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

python manage.py runserver 127.0.0.1:8000

pause 