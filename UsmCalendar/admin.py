from django.contrib import admin
from .models import Evento, Segmento
from django.contrib.auth.models import Group
from django.db.models.signals import post_save # Importa una señal que se ejecuta cuando se guarda un modelo.
from django.dispatch import receiver # Importa un decorador que se usa para ejecutar una función cuando se recibe una señal.

# Cuando se guarda un modelo Segmento, se ejecuta esta función.
@receiver(post_save, sender=Segmento)
def crearGrupo(sender, instance, created, **kwargs):
    if created:
        nombreSegmento = instance.nombre
        # Si el grupo no existe lo crea
        if not Group.objects.filter(name=nombreSegmento).exists():
            Group.objects.create(name=nombreSegmento)

# Register your models here.

admin.site.register(Evento)
admin.site.register(Segmento)
