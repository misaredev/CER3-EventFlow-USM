"""
URL configuration for EventFlow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from UsmCalendar import views

=======
from rest_framework.documentation import include_docs_urls  #importa documentacion automatica de api
>>>>>>> 9ccf081554efd47e5c4b96760bcb52ba389099ad


urlpatterns = [
    path('', views.index, name='inicio'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('doc/', include_docs_urls(title='Documentacion de API')), #mas que nada es para tenerlo bonito
]
