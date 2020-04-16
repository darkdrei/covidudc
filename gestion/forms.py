from django import forms
from .models import RespuestaUsuario, Encuesta, PlantillaEncuesta


class RespuestaUsuarioForm(forms.ModelForm):
    class Meta:
        model = RespuestaUsuario
        fields = ['pregunta', 'respuesta']    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-contact'
            })
            

class PlantillaEncuestaForm(forms.ModelForm):
    class Meta:
        model = PlantillaEncuesta
        fields = ['preguntas']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-contact'
            })


#Examen.objects.get(id=2).plantillaExamen.preguntas.all()
class EncuestaForm(forms.ModelForm):
    
    class Meta:
        queryset = PlantillaEncuesta.objects.first().preguntas.all()
        preguntas = forms.ModelChoiceField(queryset)
        model = Encuesta    
        fields = ['plantillaEncuesta']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-contact'
            })   