# Generated by Django 2.1.15 on 2020-06-18 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuarios_ult_modificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosUsuario',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estados_usuario',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='tipodocumento',
            options={'verbose_name': 'Tipo documento', 'verbose_name_plural': 'Tipos de documento'},
        ),
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['primernombre'], 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id_estado',
            field=models.ForeignKey(db_column='id_estado', default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.EstadosUsuario'),
            preserve_default=False,
        ),
    ]
