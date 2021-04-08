"""Breakingbad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from aplicaciones.views import prueba, temporadas, index, capitulo, personaje


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('aplicaciones.urls')),
    path('prueba/', prueba),
    path('temporadas/', temporadas),
    path('temporadas/index/<name_serie>/<n_temporada>', index),    
    path('capitulo/<id_capitulo>', capitulo),
    path('personaje/<name_personaje>', personaje),
]
