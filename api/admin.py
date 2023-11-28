from django.contrib import admin
from rest_framework import permissions

# Register your models here.

class Permisos_seguro_e_inseguro(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Permitir todos los métodos seguros
            return True
        elif request.user.is_authenticated and request.user.groups.filter(name='developer').exists():
            # Permitir acciones POST, PUT y DELETE solo a usuarios autenticados con el grupo "developer"
            return True
        return False
        