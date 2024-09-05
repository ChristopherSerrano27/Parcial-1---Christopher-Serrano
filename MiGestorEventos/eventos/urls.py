from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventos_lista, name='eventos_lista'),
]
