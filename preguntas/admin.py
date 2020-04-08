from django.contrib import admin
from preguntas import models
from .models import Sintoma, Pregunta, Observacion, Recomendacion, Clasificador, PreguntaClasificador
from gestion import admin as a_gestion
from gestion.models import RespuestaUsuario, Valoracion

# Register your models here.

class RespuestaUsuarioInlineAdmin(admin.TabularInline):
    model = RespuestaUsuario
    extra = 0


class SintomaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']
admin.site.register(models.Sintoma, SintomaAdmin)


class SintomaInlineAdmin(admin.TabularInline):
    model = Pregunta.sintomas.through
    extra = 3
    

class PreguntaClasificadorInlineAdmin(admin.TabularInline):
    model = PreguntaClasificador
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'get_sintomas', 'posicion']
    search_fields = ['nombre', 'descripcion']
    fields = ['nombre', 'descripcion', 'posicion']
    list_filter = ['sintomas', 'posicion']
    list_editable = ['posicion']
    inlines = [RespuestaUsuarioInlineAdmin, SintomaInlineAdmin, PreguntaClasificadorInlineAdmin]

    def get_sintomas(self, obj):
        return ", ".join([sintoma.nombre for sintoma in obj.sintomas.all()])
    get_sintomas.short_description = "Sintomas"
admin.site.register(models.Pregunta, PreguntaAdmin)


class RecomendacionObservacionInlineAdmin(admin.TabularInline):
    model = Observacion
    extra = 1
    

class RecomendacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']
    inlines = [RecomendacionObservacionInlineAdmin]
admin.site.register(models.Recomendacion, RecomendacionAdmin)


class ObservacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'recomendacion', 'descripcion']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['recomendacion']
    list_editable = ['recomendacion']    
admin.site.register(models.Observacion, ObservacionAdmin)


class RecomendacionClasificadorInlineAdmin(admin.TabularInline):
    model = Clasificador.recomendaciones.through
    extra = 3


class ValoracionInlineAdmin(admin.TabularInline):
    model = Valoracion
    extra = 1


class ClasificadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'recomendaciones', 'atencion']
    search_fields = ['nombre', 'descripcion']
    fields = ['nombre', 'descripcion', 'atencion']
    list_filter = ['atencion', 'recomendaciones']
    list_editable = ['atencion', 'recomendaciones']
    inlines = [RecomendacionClasificadorInlineAdmin, PreguntaClasificadorInlineAdmin, ValoracionInlineAdmin]
    def recomendaciones(self, obj):
        return ", ".join([recomendacion.nombre for recomendacion in obj.recomendaciones.all()])
    recomendaciones.short_description = "Recomendaciones"
admin.site.register(models.Clasificador, ClasificadorAdmin)


class PreguntaClasificadorAdmin(admin.ModelAdmin):
    list_display = ['clasificador', 'pregunta', 'respuesta']
    list_filter = ['pregunta', 'respuesta']
    list_editable = ['respuesta', 'pregunta']
admin.site.register(models.PreguntaClasificador, PreguntaClasificadorAdmin)