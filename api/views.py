from rest_framework import viewsets
from .serializer import EventoSerializer
from UsmCalendar.models import Evento

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    def get_queryset(self):
        queryset = Evento.objects.all() #obtiene todo
        fecha_inicio = self.request.query_params.get('fecha_inicio', None)
        tipo = self.request.query_params.get('tipo', None)
        segmento = self.request.query_params.get('segmento', None)
        
        #filtro por año, tipo y segmento
        if fecha_inicio is not None:
            queryset = queryset.filter(año=fecha_inicio)
        if tipo is not None:
            queryset = queryset.filter(tipo=tipo)
        if segmento is not None:
            queryset = queryset.filter(segmento=segmento)
        
        return queryset