from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Contacto

class ContactoCreateView(CreateView):
    model = Contacto
    fields = ['nombre', 'email', 'mensaje']
    template_name = 'formulario/contacto_form.html'
    success_url = reverse_lazy('contacto_exito')

from django.views.generic import TemplateView
class ContactoExitoView(TemplateView):
    template_name = 'formulario/contacto_exito.html'

# --- API REST ---
from rest_framework import generics
from .serializers import ContactoSerializer

class ContactoListAPI(generics.ListAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
