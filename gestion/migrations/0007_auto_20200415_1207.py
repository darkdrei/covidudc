# Generated by Django 3.0.5 on 2020-04-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_auto_20200415_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestausuario',
            name='respuesta',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO'), ('--Seleccione--', 'BLANCO')], default='--Seleccione--', max_length=15),
        ),
    ]