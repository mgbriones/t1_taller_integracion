from django.urls import path
from .views import home, contacto, prueba

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
]
