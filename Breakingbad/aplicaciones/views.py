from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    return render(request,'aplicaciones/home.html')


def contacto(request):
    return render(request,'aplicaciones/contacto.html')


#puede que tenga que borrarla

def api():
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters/1'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        #print("\n\n@@&&========================\nFUNCIONO\n\n")
        print('\n\n@@@@@@@@@@@@@@@@@@@@@@@')
        print(content)
        return content


def prueba(request):
    
    return HttpResponse(api())



