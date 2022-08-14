from msilib.schema import ListView
from django.shortcuts import render
from flores.models import Productos
from django.views.generic import ListView, DetailView

# Vistas:

# Inicio:
def inicio(request):
    return render(request, 'flores/index.html')

# Listado de productos:
class ProductosLista(ListView):
    model = Productos
    template_name = 'flores/productos_lista.html'

# Detalles de los productos:
class ProductosDetalle(DetailView):
    model = Productos
    template_name = 'flores/productos_detalle.html'