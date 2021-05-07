from django.shortcuts import render
from django.views import generic
from .models import RespuestaUsuario, Encuesta, PlantillaEncuesta
from .forms import RespuestaUsuarioForm, EncuestaForm, PlantillaEncuestaForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.forms import modelformset_factory


class EncuestaNew(generic.CreateView):
    model = Encuesta
    template_name = 'gestion/index.html'
    context_object_name = "obj"
    form_class = EncuestaForm
    success_url = reverse_lazy("gestion:encuesta")    

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(EncuestaNew, self).get_context_data(**kwargs)
        context["lista_preguntas"] = PlantillaEncuesta.objects.first().preguntas.all()
        return context
    
    

# def Index(request):
#     encuesta = RespuestaUsuario.objects.all()
#     context = {'encuesta': encuesta}
#     return render(request, 'gestion/index.html', context)


# def Index(request):
#     form_set1 = modelformset_factory(RespuestaUsuario, fields=('pregunta', 'respuesta'))
#     form = form_set1
#     return render(request, 'gestion/index.html', {'form':form})

#def index(request):
    