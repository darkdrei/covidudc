from django.contrib import admin
from gestion import models


class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta']
    list_filter = ['pregunta', 'respuesta']
admin.site.register(models.RespuestaUsuario, RespuestaUsuarioAdmin)


class RespuestaUsuarioInlineAdmin(admin.TabularInline):
    model = models.Valoracion.respuestas.through
    extra = 1


class ValoracionAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'clasificacion', 'get_respuestas']
    search_fields = ['fecha']
    list_filter = ['respuestas', 'clasificacion']
    
    fields = ['clasificacion']
    inlines = [RespuestaUsuarioInlineAdmin]
    
    def get_respuestas(self, obj):
        return ", ".join([str(respuesta_usuario) for respuesta_usuario in obj.respuestas.all()])
    get_respuestas.short_description = "Respuestas"
admin.site.register(models.Valoracion, ValoracionAdmin)    
        

class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'valoracion_inicial', 'fecha']
    search_fields = ['fecha']
    list_filter = ['paciente', 'medico', 'valoracion_inicial']
admin.site.register(models.Diagnostico, DiagnosticoAdmin)
    