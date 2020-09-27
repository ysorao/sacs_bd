from django.db import models
from django.forms import ModelForm

      
class Usuarios(models.Model):
    idusuario = models.AutoField(primary_key=True)
    primernombre = models.CharField(db_column='primerNombre', max_length=45)  # Field name made lowercase.
    segundonombre = models.CharField(db_column='segundoNombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='primerApellido', max_length=45)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='segundoApellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.IntegerField(db_column='numeroDocumento', unique=True)  # Field name made lowercase.
    contrasena = models.CharField(max_length=45)
    fecharegistro = models.DateTimeField(db_column='fechaRegistro', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    ult_modificacion = models.DateTimeField(auto_now=True)
    id_tipo_documento = models.OneToOneField('tipodocumento', on_delete = models.DO_NOTHING, db_column='id_tipo_documento')
    id_estado = models.OneToOneField('estadosusuario', on_delete = models.DO_NOTHING, db_column='id_estado')

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        ordering = ['primernombre']

    def __str__(self):
        return self.primernombre
    

class EstadosUsuario(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=50)

    class Meta:
        db_table = 'estados_usuario'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre_estado


class TipoDocumento(models.Model):
    idtipo_documento = models.IntegerField(primary_key=True)
    nombredocumento = models.CharField(db_column='nombreDocumento', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'tipo_documento'
        verbose_name = 'Tipo documento'
        verbose_name_plural = 'Tipos de documento'

    def __str__(self):
        return self.nombredocumento
