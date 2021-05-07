from django.contrib import admin
from gestion import models


class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta']
    list_filter = ['pregunta', 'respuesta']
admin.site.register(models.RespuestaUsuario, RespuestaUsuarioAdmin)


class ValoracionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'clasificacion', 'encuesta']
    search_fields = ['fecha']
    list_filter = ['encuesta', 'clasificacion']        
admin.site.register(models.Valoracion, ValoracionAdmin)    
        

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'valoracion_inicial', 'fecha']
    search_fields = ['fecha']
    list_filter = ['paciente', 'medico', 'valoracion_inicial']
admin.site.register(models.Diagnostico, DiagnosticoAdmin)


admin.site.register(models.PlantillaEncuesta)
admin.site.register(models.Encuesta)