@echo off
echo Iniciando servidor de desarrollo...
echo URL: http://127.0.0.1:8000/
echo.
call venv\Scripts\activate.bat
python manage.py runserver 127.0.0.1:8000 