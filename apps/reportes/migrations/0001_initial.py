# Generated by Django 3.0.8 on 2020-07-22 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasesDatos',
            fields=[
                ('id_bd', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bd', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Base de datos',
                'verbose_name_plural': 'Bases de datos',
                'db_table': 'bases_datos',
                'ordering': ['nombre_bd'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instancias',
            fields=[
                ('id_instancia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_instancia', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Instancia',
                'verbose_name_plural': 'Instancias',
                'db_table': 'instancias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periodicidad',
            fields=[
                ('id_periodicidad', models.AutoField(primary_key=True, serialize=False)),
                ('frecuencia_bck', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Frecuencia',
                'verbose_name_plural': 'Frecuencias',
                'db_table': 'periodicidad',
                'ordering': ['id_periodicidad'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PoliticasBck',
            fields=[
                ('id_politica', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Políticas de backup',
                'verbose_name_plural': 'Política bck',
                'db_table': 'politicas_bck',
                'ordering': ['id_instancia'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoBckls',
            fields=[
                ('id_tipo_bck', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tipo_bck', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo de bck',
                'verbose_name_plural': 'Tipos de bck',
                'db_table': 'tipo_bckLS',
                'managed': False,
            },
        ),
    ]
