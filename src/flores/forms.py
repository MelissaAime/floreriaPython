from django.forms import Form, CharField

# Formulario de busqueda de producto:
class FormBuscarProducto(Form):
    producto_nombre = CharField(max_length=100) 