from django.http import HttpResponse

def home(request):
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bienvenido a JDApp</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gradient-to-br from-blue-800 to-blue-400 min-h-screen flex items-center justify-center">
        <div class="bg-white rounded-xl shadow-2xl p-10 max-w-md w-full text-center">
            <h1 class="text-3xl font-bold text-blue-800 mb-4">Bienvenido a <span class="text-blue-600">JDApp</span></h1>
            <p class="text-gray-700 mb-8">Esta es la página principal del sistema de gestión.<br>Accede al formulario para comenzar.</p>
            <a href="/formulario/" class="inline-block px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow hover:bg-blue-700 transition">Ir al Formulario</a>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html) 