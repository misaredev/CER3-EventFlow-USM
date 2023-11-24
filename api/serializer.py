from rest_framework import serializers
from UsmCalendar.models import Evento


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'