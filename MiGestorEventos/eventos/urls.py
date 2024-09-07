from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('eventos/', views.eventos_lista, name='eventos_lista'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),

#2.4, organizadores
    path('organizadores/', views.OrganizadoresListaView.as_view(), name= 'organizadores_lista'),
    path('organizadores/crear/', views.OrganizadorCrearView.as_view(), name= 'crear_organizador'),

#2.5, editar eventos
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:pk>/', views.eliminar_evento, name='eliminar_evento'),
]
