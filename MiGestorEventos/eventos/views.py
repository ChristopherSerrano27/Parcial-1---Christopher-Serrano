from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm

def eventos_lista(request):
    eventos = Evento.objects.select_related('organizador').all()
    return render(request, 'eventos_lista.html', {'eventos': eventos})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos_lista')  # Redirige a la lista de eventos después de guardar
    else:
        form = EventoForm()
    
    return render(request, 'crear_evento.html', {'form': form})