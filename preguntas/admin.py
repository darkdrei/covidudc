from django.contrib import admin
from preguntas import models

# Register your models here.


class SintomaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']
admin.site.register(models.Sintoma, SintomaAdmin)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'get_sintomas','posicion']
    search_fields = ['nombre', 'sintomas']

    def get_sintomas(self, obj):
        return ", ".join([sintoma.nombre for sintoma in obj.sintomas.all()])
    get_sintomas.short_description = "Sintomas"
admin.site.register(models.Pregunta, PreguntaAdmin)


class RecomendacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']
admin.site.register(models.Recomendacion, RecomendacionAdmin)


class ObservacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'recomendacion', 'descripcion']
    search_fields = ['nombre', 'recomendacion', 'descripcion']
admin.site.register(models.Observacion, ObservacionAdmin)


class ClasificadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'get_recomendaciones', 'atencion']
    search_fields = ['nombre', 'descripcion', 'recomendaciones', 'atencion']
    
    def get_recomendaciones(self, obj):
        return ", ".join([recomendacion.nombre for recomendacion in obj.recomendaciones.all()])
    get_recomendaciones.short_description = "Recomendaciones"
admin.site.register(models.Clasificador, ClasificadorAdmin)


class PreguntaClasificadorAdmin(admin.ModelAdmin):
    list_display = ['clasificador', 'pregunta', 'respuesta']
    search_fields = ['clasificador', 'pregunta', 'respuesta']
admin.site.register(models.PreguntaClasificador, PreguntaClasificadorAdmin)