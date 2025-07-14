Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Iniciando JDApp - Servidor Local" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. Activando entorno virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "2. Verificando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "3. Ejecutando migraciones..." -ForegroundColor Yellow
python manage.py migrate

Write-Host ""
Write-Host "4. Recolectando archivos estáticos..." -ForegroundColor Yellow
python manage.py collectstatic --noinput

Write-Host ""
Write-Host "5. Iniciando servidor de desarrollo..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Servidor iniciado en: http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

python manage.py runserver 127.0.0.1:8000 