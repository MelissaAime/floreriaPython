from django.urls import path
from profileuser.views import *

urlpatterns = [
    path("editar/", editar_perfil, name="editar_perfil")
]