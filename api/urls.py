from django.urls import path, include
from rest_framework import routers
from .views import EventoViewSet

routers = routers.DefaultRouter()
routers.register(r'evento', EventoViewSet) 
# la 'r' es para que al crear la pagina no quede como '/n' cosa que se podria identificar como salto de linea 

urlpatterns = [
    path('', include(routers.urls)),
]
