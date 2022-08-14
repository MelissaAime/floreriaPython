from django.urls import path
from flores.views import *

urlpatterns = [
    path("", inicio, name="flores_inicio"),
    path("productos", ProductosLista.as_view(), name="flores_productos"),
    path("productos/<pk>", ProductosDetalle.as_view(), name="flores_productos_detalle"),
]