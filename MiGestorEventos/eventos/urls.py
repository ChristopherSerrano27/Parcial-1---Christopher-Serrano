from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos_lista, name='eventos_lista'),
    path('crear/', views.crear_evento, name='crear_evento'),
]
