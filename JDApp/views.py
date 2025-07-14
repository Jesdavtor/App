from django.http import HttpResponse

def home(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JDApp</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-gradient-to-br from-blue-800 to-blue-400 min-h-screen flex items-center justify-center p-4">
        <div class="bg-white rounded-xl shadow-2xl p-8 max-w-lg w-full text-center">
            <div class="mb-6">
                <h1 class="text-4xl font-bold text-blue-800 mb-2">JDApp</h1>
            </div>
            
            <p class="text-gray-700 mb-8 text-lg">Bienvenido al panel de administración. Selecciona una opción para comenzar:</p>
            
            <div class="space-y-4">
                <a href="/formulario/" class="block w-full px-6 py-4 bg-blue-600 text-white font-semibold rounded-lg shadow hover:bg-blue-700 transition duration-200 text-center">
                    <i class="fas fa-clipboard-list mr-2"></i>
                    Formulario de Contacto
                </a>
                
                <a href="/admin/" class="block w-full px-6 py-4 bg-green-600 text-white font-semibold rounded-lg shadow hover:bg-green-700 transition duration-200 text-center">
                    <i class="fas fa-cog mr-2"></i>
                    Panel de Administración
                </a>
                
                <a href="/swagger/" class="block w-full px-6 py-4 bg-purple-600 text-white font-semibold rounded-lg shadow hover:bg-purple-700 transition duration-200 text-center">
                    <i class="fas fa-book mr-2"></i>
                    Documentación API
                </a>
            </div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)