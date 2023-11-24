from rest_framework import viewsets
from .serializer import EventoSerializer
from UsmCalendar.models import Evento

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer