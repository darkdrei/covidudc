from django.urls import path
from gestion.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
