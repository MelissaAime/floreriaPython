from django.shortcuts import render, redirect

# Formulario inicio sesion, crear usuario y autenticacion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from authentication.forms import UserRegisterForm

# Loguearse:
def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {"form": form})
    else:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("flores_inicio")
        
        form = AuthenticationForm()
        return render(request, 'authentication/login.html', {"form": form})


#Registrarse
def register_view(request):
    if request.method == "GET":
        form = UserRegisterForm()
        return render(request, "authentication/register.html", {"form": form})
    
    else:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        
        else:
            return render(request, "authentication/register.html", {"form": form, "error": "Usuario no válido"})
        

#Desloguearse
def logout_view(request):
    logout(request)
    return redirect("flores_inicio")