from django.db import models


class PoliticasBck(models.Model):
    id_politica = models.AutoField(primary_key=True)
    id_bd = models.ForeignKey('BasesDatos', models.DO_NOTHING, db_column='id_bd')
    id_instancia = models.ForeignKey('Instancias', models.DO_NOTHING, db_column='id_instancia')
    id_tipobck = models.ForeignKey('TipoBckls', models.DO_NOTHING, db_column='id_tipobck')
    id_frecuencia_bck = models.ForeignKey('Periodicidad', models.DO_NOTHING, db_column='id_frecuencia_bck')

    class Meta:
        managed = False
        db_table = 'politicas_bck'
        unique_together = (('id_bd', 'id_instancia', 'id_frecuencia_bck'),)
        verbose_name = 'Políticas de backup'
        verbose_name_plural = 'Política bck'
        ordering = ['id_instancia']

    def __str__(self):
       return self.id_instancia.nombre_instancia + ' ' + self.id_bd.nombre_bd + ' ' + 'Backup ' + self.id_tipobck.nombre_tipo_bck + ' ' + self.id_frecuencia_bck.frecuencia_bck


class Periodicidad(models.Model):
    id_periodicidad = models.AutoField(primary_key=True)
    frecuencia_bck = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'periodicidad'
        verbose_name = 'Frecuencia'
        verbose_name_plural = 'Frecuencias'
        ordering = ['id_periodicidad']

    def __str__(self):
       return self.frecuencia_bck



class BasesDatos(models.Model):
    id_bd = models.AutoField(primary_key=True)
    nombre_bd = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bases_datos'
        verbose_name = 'Base de datos'
        verbose_name_plural = 'Bases de datos'
        ordering = ['nombre_bd']

    def __str__(self):
        return self.nombre_bd


class TipoBckls(models.Model):
    id_tipo_bck = models.IntegerField(primary_key=True)
    nombre_tipo_bck = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_bckLS'
        verbose_name = 'Tipo de bck'
        verbose_name_plural = 'Tipos de bck'

    def __str__(self):
        return self.nombre_tipo_bck


class Instancias(models.Model):
    id_instancia = models.IntegerField(primary_key=True)
    nombre_instancia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'instancias'
        verbose_name = 'Instancia'
        verbose_name_plural = 'Instancias'
    
    def __str__(self):
        return self.nombre_instancia

class Programacionbck(models.Model):
    IP_No_modificar = models.CharField(db_column='IP', max_length=50, blank=True, null=True, editable=False)  # Field name made lowercase.
    Server_Name_No_modificar = models.CharField(db_column='SERVER_NAME', max_length=50, blank=True, null=True, editable=False)  # Field name made lowercase.
    Lunes_a_Sábado = models.IntegerField(db_column='CANT_L_S', blank=True, null=True)  # Field name made lowercase.
    Domingo = models.IntegerField(db_column='CANT_DMG', blank=True, null=True)  # Field name made lowercase.
    Mensual = models.IntegerField(db_column='CANT_MENSUAL', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'programacionBck'
        verbose_name = 'Programación'
        verbose_name_plural = 'Programación copias diarias por instancia'
        ordering = ['Server_Name_No_modificar']

    def __str__(self):
        return self.IP_No_modificar+' / '+self.Server_Name_No_modificar