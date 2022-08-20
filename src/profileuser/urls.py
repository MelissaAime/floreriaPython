from django.urls import path
from profileuser.views import *

urlpatterns = [
    path("perfil/", perfil, name="perfil"),
    path("editar/", editar_perfil, name="editar_perfil"),
    path("avatar/", agregar_avatar, name="avatar")
]