from django.urls import path
from authentication.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
]