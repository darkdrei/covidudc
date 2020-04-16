from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone 

# Create your models here.
from preguntas import models as m_pregunta
from gestion.choices import SI_NO



class RespuestaUsuario(models.Model):
    pregunta = models.ForeignKey(m_pregunta.Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(choices=SI_NO, default=SI_NO.BLANCO, max_length=15)

    def __str__(self):
        return '{pregunta} / {respuesta}'.format(pregunta=self.pregunta.nombre, respuesta=self.respuesta)

    class Meta:
        verbose_name = 'Respuesta de usuario'
        verbose_name_plural = 'Respuestas de usuarios'
    
    def respuestas_cho(self):
        return dict(RespuestaUsuario.SI_NO)[self.respuesta]


class PlantillaEncuesta(models.Model):
    preguntas = models.ManyToManyField(RespuestaUsuario)
    
    class Meta:
        verbose_name = 'Plantilla de encuesta'
        verbose_name_plural = 'Plantillas de encuestas'
    

class Encuesta(models.Model):
    plantillaEncuesta = models.ForeignKey(PlantillaEncuesta, on_delete=models.CASCADE, blank=True, null=True)
    fechaEncuesta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{complemento}{numero}'.format(complemento='0'*(10-len(str(self.id))),numero=self.id)
    
    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'


class Valoracion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, blank=True, null=True)
    clasificacion = models.ForeignKey(m_pregunta.Clasificador, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{complemento}{numero}'.format(complemento='0'*(10-len(str(self.id))),numero=self.id)

    class Meta:
        verbose_name = 'Valoración'
        verbose_name_plural = 'Valoraciones'


class Diagnostico(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paciente')
    medico = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medico')
    valoracion_inicial = models.ForeignKey(Valoracion, on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{paciente}'.format(paciente=self.paciente.first_name + ' '+self.paciente.last_name)

    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
