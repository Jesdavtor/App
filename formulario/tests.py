from django.test import TestCase
from django.urls import reverse
from .models import Contacto

# Create your tests here.

class ContactoModelTest(TestCase):
    def test_crear_contacto(self):
        contacto = Contacto.objects.create(nombre='Juan', email='juan@email.com', mensaje='Hola, esto es una prueba.')
        self.assertEqual(str(contacto), 'Juan (juan@email.com)')

class ContactoViewTest(TestCase):
    def test_formulario_contacto_get(self):
        response = self.client.get(reverse('formulario_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contacto')

    def test_formulario_contacto_post_valido(self):
        data = {'nombre': 'Ana', 'email': 'ana@email.com', 'mensaje': 'Mensaje de prueba largo.'}
        response = self.client.post(reverse('formulario_home'), data)
        self.assertRedirects(response, reverse('contacto_exito'))
        self.assertEqual(Contacto.objects.count(), 1)

    def test_formulario_contacto_post_invalido(self):
        data = {'nombre': '', 'email': 'noemail', 'mensaje': 'corto'}
        response = self.client.post(reverse('formulario_home'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'nombre', 'El nombre es obligatorio.')
        self.assertFormError(response, 'form', 'email', 'Introduce un correo electrónico válido.')
        self.assertFormError(response, 'form', 'mensaje', 'El mensaje debe tener al menos 10 caracteres.')
