from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['primernombre','segundonombre','primerapellido','segundoapellido','numerodocumento',
        'contrasena','id_tipo_documento', 'id_estado']