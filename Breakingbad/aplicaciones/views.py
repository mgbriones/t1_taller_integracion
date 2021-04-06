from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.template import Context, Template

# Create your views here.
def home(request):
    
    return render(request,'aplicaciones/home.html')


def contacto(request):
    print("##########################")
    print(request)
    return render(request,'aplicaciones/contacto.html')


#puede que tenga que borrarla

def api():
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters/1'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        #print("\n\n@@&&========================\nFUNCIONO\n\n")
        print('\n\n@@@@@@@@@@@@@@@@@@@@@@@')
        print(content)
        print(content[0])
        return content


def prueba(request):
    
    return HttpResponse(api())

def temporadas(request):

    #se carga el template
    #doc_externo = open("C:/Users/Matias Briones/Desktop/t1_taller_integracion/Breakingbad/aplicaciones/templates/aplicaciones/temporadas.html")
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/temporadas.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()

    #ctx = Context()
    algo = api()
    print("PASO X AQUI")
    print(algo)
    print('============')
    ctx = Context({"consulta": algo, "papa":"padre"})

    documento = plt.render(ctx)



    return HttpResponse(documento)


