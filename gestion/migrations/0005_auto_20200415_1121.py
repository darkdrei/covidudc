# Generated by Django 3.0.5 on 2020-04-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20200414_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encuesta',
            old_name='modeloEncuesta',
            new_name='plantillaEncuesta',
        ),
        migrations.RemoveField(
            model_name='valoracion',
            name='respuestas',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fechaEncuesta',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='encuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.Encuesta'),
        ),
    ]