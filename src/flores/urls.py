from django.urls import path
from flores.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("productos", ProductosLista.as_view(), name="productos"),
    path("productos/<pk>", ProductosDetalle.as_view(), name="productos_detalle"),
]