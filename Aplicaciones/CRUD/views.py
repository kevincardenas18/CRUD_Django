from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

# Create your views here.

def home(request):
    listaUsuarios = Usuario.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": listaUsuarios})

def registrarUsuario(request):
    codigo = request.POST['txtCodigo']
    usuario = request.POST['txtUsuario']
    password = request.POST['txtPassword']
    
    usuario = Usuario.objects.create(codigo=codigo, usuario=usuario, password=password)
    return redirect('/')

def edicionUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo = codigo)
    return render(request, "editarUsuario.html", {"usuario":usuario})

def editarUsuario(request):
    codigo = request.POST['txtCodigo']
    usuarioEdit = request.POST['txtUsuario']
    password = request.POST['txtPassword']

    usuario = Usuario.objects.get(codigo = codigo)
    usuario.usuario = usuarioEdit
    usuario.password = password
    usuario.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/')

def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo = codigo)
    usuario.delete()

    return redirect('/')