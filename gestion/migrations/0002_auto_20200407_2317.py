# Generated by Django 3.0.5 on 2020-04-08 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostico',
            options={'verbose_name': 'Diagnóstico', 'verbose_name_plural': 'Diagnósticos'},
        ),
        migrations.AlterModelOptions(
            name='respuestausuario',
            options={'verbose_name': 'Respuesta de usuario', 'verbose_name_plural': 'Respuestas de usuarios'},
        ),
    ]
