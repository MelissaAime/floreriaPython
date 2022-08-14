from django.forms import CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Sesiones
class UserRegisterForm(UserCreationForm):

    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Confirmar contraseña', widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {"username": "", "password1": "", "password2": ""}