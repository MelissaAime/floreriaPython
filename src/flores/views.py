from django.shortcuts import render
from flores.models import Productos
from flores.forms import FormBuscarProducto
from django.views.generic import ListView, DetailView

# Requerimiento de login 
from django.contrib.auth.mixins import LoginRequiredMixin

# Vistas:

# Inicio:
def inicio(request):
    return render(request, 'flores/index.html')

# Acerca de mi:
def acercademi(request):
    return render(request, 'flores/acercademi.html')

# Busqueda de productos:
def productos_buscar(request):
    
    productos_lista = Productos.objects.all()

    if request.GET.get('producto_nombre'):

        formProducto = FormBuscarProducto(request.GET)

        if formProducto.is_valid():
            data = formProducto.cleaned_data
            productos_lista = Productos.objects.filter(nombre__icontains = data['producto_nombre'])

        return render(request, 'flores/productos_lista.html', {"productos_buscar": productos_lista, "form": formProducto})
    
    else:
        formProducto = FormBuscarProducto()
        return render(request, 'flores/productos_lista.html', {"productos_buscar": productos_lista, "form": formProducto})


# Detalles de los productos:
# Solo visible al estar logueado
class ProductosDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    template_name = 'flores/productos_detalle.html'