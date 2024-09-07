from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm, OrganizadorForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, DeleteView
from .models import Organizador
from django.contrib import messages

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

#PUNTO 2.5
@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos_lista')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "El evento ha sido eliminado.")
        return redirect('eventos_lista')
    return render(request, 'confirmar_eliminacion.html', {'object': evento})

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')