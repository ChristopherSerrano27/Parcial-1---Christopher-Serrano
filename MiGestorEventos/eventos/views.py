from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm, OrganizadorForm

from django.views.generic import ListView, CreateView
from .models import Organizador

def eventos_lista(request):
    eventos = Evento.objects.select_related('organizador').all()
    return render(request, 'eventos_lista.html', {'eventos': eventos})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos_lista')  
    else:
        form = EventoForm()
    
    return render(request, 'crear_evento.html', {'form': form})

#PUNTO 2.4

class OrganizadoresListaView(ListView):
    model = Organizador
    template_name = 'organizadores_lista.html'
    context_object_name = 'organizadores'

class OrganizadorCrearView(CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'crear_organizador.html'
    success_url = '/organizadores/'