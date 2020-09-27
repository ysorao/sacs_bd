from django.contrib import admin
from .models import TipoDocumento,Usuarios,EstadosUsuario

admin.site.register(TipoDocumento)
admin.site.register(Usuarios)
admin.site.register(EstadosUsuario)