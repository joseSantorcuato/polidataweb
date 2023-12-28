from django.urls import path
from . import views

urlpatterns = [
    path('patrones/', views.patrones, name='patrones'),
    path('', views.home, name='home'),  # Ruta vacía para la página principal
    path('evaluacion/', views.evaluacion, name='evaluacion'),
    path('sistemas/', views.sistemas, name='sistemas'),
    path('aprendizaje/', views.aprendizaje, name='aprendizaje'),
]