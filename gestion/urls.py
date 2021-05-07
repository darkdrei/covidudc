from django.urls import path

from .views import EncuestaNew

urlpatterns = [
    path('', EncuestaNew.as_view(), name='encuesta'),
]
