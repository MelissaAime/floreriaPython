from django.shortcuts import render, redirect
from profileuser.forms import UserEditForm, AvatarForm
from profileuser.models import Avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Mostrar perfil y avatar
@login_required
def perfil(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, "profileuser/perfil.html", {"avatar": avatar.imagen.url})


# Editar perfil del usuario
@login_required
def editar_perfil(request):

    if request.method == "GET":
        formPerfil = UserEditForm(initial = {"email": request.user.email, 
                                            "first_name": request.user.first_name, 
                                            "last_name": request.user.last_name
                                            })
        return render(request, "profileuser/editar_perfil.html", {"formPerfil": formPerfil})
    
    else:
        formPerfil = UserEditForm(request.POST)

        if formPerfil.is_valid():
            data = formPerfil.cleaned_data

            usuario = request.user
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
        
        return redirect("flores_inicio")


# Agregar un avatar
@login_required
def agregar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method == "GET":
        formAvatar = AvatarForm()
        contexto = {"formAvatar": formAvatar, "avatar": avatar.imagen.url}
        return render(request, "profileuser/agregar_avatar.html", contexto)
        
    else:
        formAvatar = AvatarForm(request.POST, request.FILES)

        if formAvatar.is_valid():
            data = formAvatar.cleaned_data

            user = User.objects.filter(username=request.user.username).first()

            avatar = Avatar(user=user, imagen=data["imagen"])

            avatar.save()
            return redirect("flores_inicio")
        return render(request, "profileuser/agregar_avatar.html", {"formAvatar": formAvatar})



