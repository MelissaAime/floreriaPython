from django.forms import Form, IntegerField, CharField, EmailField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Editar usuario
class UserEditForm(UserCreationForm):
    email = EmailField(label="Nuevo email")
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Confirmar contraseña', widget=PasswordInput)
    first_name = CharField(label="Nombre")
    last_name = CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {"username": "", "email": "", "password1": "", "password2": ""}


class AvatarForm(Form):
    imagen = ImageField()
