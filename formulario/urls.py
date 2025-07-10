from django.urls import path
from .views import ContactoCreateView, ContactoExitoView, ContactoListAPI

urlpatterns = [
    path('', ContactoCreateView.as_view(), name='formulario_home'),
    path('contacto/', ContactoCreateView.as_view(), name='contacto'),
    path('contacto/exito/', ContactoExitoView.as_view(), name='contacto_exito'),
    path('api/contactos/', ContactoListAPI.as_view(), name='api_contactos'),
] 