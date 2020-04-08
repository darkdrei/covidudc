from django.db import models

# Create your models here.


class Sintoma(models.Model):
    nombre = models.CharField(unique=True, max_length=20)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        return '{nombre}'.format(nombre=self.nombre)
    
    class Meta: 
        verbose_name = 'Síntoma'
        verbose_name_plural = 'Síntomas'


class Pregunta(models.Model):
    nombre = models.TextField(max_length=800)
    descripcion = models.TextField(max_length=2000, verbose_name='Descripción', blank=True, null=True)
    sintomas = models.ManyToManyField(Sintoma, blank=True)
    posicion = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{nombre}'.format(nombre=self.nombre)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class Recomendacion(models.Model):
    nombre = models.CharField(unique=True, max_length=500)
    descripcion = models.TextField(max_length=2000, verbose_name='Descripción', blank=True, null=True)

    def __str__(self):
        return '{nombre}'.format(nombre=self.nombre)
    
    class Meta:
        verbose_name = 'Recomendación'
        verbose_name_plural = 'Recomendaciones'


class Observacion(models.Model):
    recomendacion = models.ForeignKey(Recomendacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        return '{nombre}'.format(nombre=self.nombre)

    class Meta:
        verbose_name = 'Observación'
        verbose_name_plural = 'Observaciones'


class Clasificador(models.Model):
    nombre = models.CharField(unique=True, max_length=500)
    descripcion = models.TextField(max_length=2000, verbose_name='Descripción', blank=True, null=True)
    recomendaciones = models.ManyToManyField(Recomendacion, blank=True)
    atencion = models.BooleanField(default=False, verbose_name='Requiere atención')

    def __str__(self):
        return '{nombre}'.format(nombre=self.nombre)

    class Meta:
        verbose_name = 'Clasificador'
        verbose_name_plural = 'Clasificadores'


class PreguntaClasificador(models.Model):
    clasificador = models.ForeignKey(Clasificador, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.BooleanField(default=False)

    def __str__(self):
        return '{clasificador} / {pregunta}'.format(clasificador=self.clasificador, pregunta=self.pregunta)
    
    class Meta:
        verbose_name = 'Clasificador de Pregunta'
        verbose_name_plural = 'Clasificadores de Preguntas'
        unique_together = (('clasificador', 'pregunta', 'respuesta'))

