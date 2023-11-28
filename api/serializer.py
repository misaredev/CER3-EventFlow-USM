from rest_framework import serializers
from UsmCalendar.models import Evento, Segmento, TIPO

#este serializador es para mostrar el nombre de los segmentos en vez de su id (aparecia un numero)
class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segmento
        fields = ['nombre']

class EventoSerializer(serializers.ModelSerializer):

    segmentos = SegmentoSerializer(many=True, read_only=True) #para añadir el serializador de arriba que muestra los nombres de los segmentos
    tipo = serializers.ChoiceField(choices=TIPO, source='get_tipo_display') #para que se muestre el nombre del tipo
    class Meta:
        model = Evento
        fields = '__all__'