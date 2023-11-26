from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):
    title = "EventFlow"
    Eventos = Evento.objects.all().order_by('fecha_inicio')

    segmento = request.GET.get('selectSegmento')
    tipo = request.GET.get('selectTipo')

    if not segmento:
        segmento = "Todos"
    if not tipo:
        tipo = "Todos"

    data = {
        "title": title,
        "Eventos": Eventos,
    }

    return render(request, 'UsmCalendar/index.html', data)