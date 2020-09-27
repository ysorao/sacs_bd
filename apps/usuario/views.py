from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UsuariosForm
from .models import Usuarios
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import connection


# Vistas de la aplicación usuario

def registrarUsuario(request):
    if request.method == 'POST':
        usuarios_form = UsuariosForm(request.POST)
        print(usuarios_form)
        if usuarios_form.is_valid():
            usuarios_form.save()
            return redirect('index')
    else:
                usuarios_form = UsuariosForm()
    return render(request,'usuario/registrar-usuario.html', {'usuarios_form':usuarios_form})

class ListadoUsuarios(ListView):
    template_name = 'usuario/listar_usuarios.html'
    queryset = Usuarios.objects.all()


def editarUsuario(request, idusuario):
    usuario = Usuarios.objects.get(idusuario=idusuario)
    if request.method == 'GET':
        usuariosForm = UsuariosForm(instance=usuario)
    else:
        usuariosForm = UsuariosForm(request.POST, instance=usuario)
        if usuariosForm.is_valid():
            usuariosForm.save()
        return redirect('index')
    return render(request, 'usuario/editar_usuario.html',{'usuDatos': usuariosForm})
