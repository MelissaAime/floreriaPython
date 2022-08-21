from django.shortcuts import render
from mensajes.models import Mensajes
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Mensajes

# Crear mensaje nuevo
class MensajeNuevo(LoginRequiredMixin, CreateView):
    model = Mensajes
    success_url = "/mensajes/leer/"
    fields = ['nombre', 'email', 'mensaje']

# Leer los mensajes
class MensajeLista(LoginRequiredMixin, ListView):
    model = Mensajes
    template_name = "mensajes/mensajes_list.html"

# Borrar los mensajes
class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensajes
    success_url = "/mensajes/leer/"