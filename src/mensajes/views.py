from django.shortcuts import render
from mensajes.models import Mensajes
from django.views.generic import CreateView, ListView, DeleteView


# Mensajes

# Crear mensaje nuevo
class MensajeNuevo(CreateView):
    model = Mensajes
    success_url = "/mensajes/leer/"
    fields = ['nombre', 'email', 'mensaje']

# Leer los mensajes
class MensajeLista(ListView):
    model = Mensajes
    template_name = "mensajes/mensajes_list.html"

# Borrar los mensajes
class MensajeBorrar(DeleteView):
    model = Mensajes
    success_url = "/mensajes/leer/"