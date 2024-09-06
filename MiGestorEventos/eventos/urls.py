from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.eventos_lista, name='eventos_lista'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),

#2.4, organizadores

    path('organizadores/', views.OrganizadoresListaView.as_view(), name= 'organizadores_lista'),
    path('organizadores/crear/', views.OrganizadorCrearView.as_view(), name= 'crear_organizador'),
]
