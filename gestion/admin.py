from django.contrib import admin
from gestion import models

# Register your models here.

class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta']
    search_fields = ['pregunta', 'respuesta']
admin.site.register(models.RespuestaUsuario, RespuestaUsuarioAdmin)


class ValoracionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'clasificacion', 'get_respuestas']
    search_fields = ['fecha', 'clasificacion', 'respuestas']
    
    def get_respuestas(self, obj):
        return ", ".join([str(respuesta_usuario) for respuesta_usuario in obj.respuestas.all()])
    get_respuestas.short_description = "Respuestas"
admin.site.register(models.Valoracion, ValoracionAdmin)    
        

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'valoracion_inicial', 'fecha']
    search_fields = ['paciente', 'medico', 'valoracion_inicial', 'fecha']
admin.site.register(models.Diagnostico, DiagnosticoAdmin)
    
"""
list_display = 
    search_fields = 
"""