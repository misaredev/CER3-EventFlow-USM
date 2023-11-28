from django.urls import path, include
from rest_framework import routers
from .views import EventoViewSet

evento_router = routers.DefaultRouter()
evento_router.register(r'evento', EventoViewSet, basename='evento')
# la 'r' es para que al crear la pagina no quede como '/n' cosa que se podria identificar como salto de linea 

urlpatterns = [
    path('', include(evento_router.urls)),
]
