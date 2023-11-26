from django.shortcuts import render
from .models import Evento, Segmento

# Create your views here.

def index(request):
    title = "EventFlow"
    Eventos = Evento.objects.all().order_by('fecha_inicio')
    Segmentos = Segmento.objects.all()

    segmento = request.GET.get('selectSegmento')
    tipo = request.GET.get('selectTipo')

    if not segmento:
        segmento = "Todos"
    if not tipo:
        tipo = "Todos"

    data = {
        "title": title,
        "Eventos": Eventos,
        "Segmentos": Segmentos,
    }

    return render(request, 'UsmCalendar/index.html', data)