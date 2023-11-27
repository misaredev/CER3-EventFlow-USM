from django.contrib import admin
from rest_framework import permissions

# Register your models here.


class Isdeveloper(permissions.BasePermission):

    def has_permission(self, request, view):
        #la ultima condicion es para que los superusuarios puedan entrar porque no me dejaba xd
        return request.user.groups.filter(name='developer').exists() or request.user.is_superuser 

