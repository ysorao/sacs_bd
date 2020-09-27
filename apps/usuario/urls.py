from django.urls import path
from .views import registrarUsuario, ListadoUsuarios, editarUsuario 

urlpatterns = [
    path('registrar-usuario/', registrarUsuario, name='registrar-usuario'),
    path('listar_usuarios/',ListadoUsuarios.as_view(),name='listar_usuarios'),
    path('editar_usuario/<int:idusuario>', editarUsuario, name='editar_usuario')
]
