from django.shortcuts import render
from .models import Evento

def eventos_lista(request):
    eventos = Evento.objects.select_related('organizador').all()
    return render(request, 'eventos_lista.html', {'eventos': eventos})
