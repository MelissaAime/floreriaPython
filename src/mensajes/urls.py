from django.urls import path
from mensajes.views import *

urlpatterns = [
    path("leer/", MensajeLista.as_view(), name="mensajes"),
    path("enviar/", MensajeNuevo.as_view(), name="enviar_mensajes"),
    path("borrar/<pk>", MensajeBorrar.as_view(), name="borrar_mensaje"),
]