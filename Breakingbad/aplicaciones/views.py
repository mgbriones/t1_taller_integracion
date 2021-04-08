from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.template import Context, Template


#modulos creados
from aplicaciones.funciones_temporada import dic_temporadas




# Create your views here.
def home(request):
    
    return render(request,'aplicaciones/home.html')


def contacto(request):
    print("##########################")
    print(request)
    return render(request,'aplicaciones/contacto.html')


#puede que tenga que borrarla

def api(url):
    #url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters/1'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        #print("\n\n@@&&========================\nFUNCIONO\n\n")
        print('\n\n@@@@@@@@@@@@@@@@@@@@@@@')
        print(content)
        print(content[0])
        return content


def prueba(request):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters/1'
    return HttpResponse(api(url))
    

def temporadas(request):

    #se carga el template
    #doc_externo = open("C:/Users/Matias Briones/Desktop/t1_taller_integracion/Breakingbad/aplicaciones/templates/aplicaciones/temporadas.html")
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/temporadas.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()

    #ctx = Context()

    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    algo = api(url)
    print("PASO X AQUI")
    #print(algo)
    print('============')


    #SE calculan la cant de tempoadas con la funcion
    dic_cant_temporadas = dic_temporadas(algo)

    list_name_temporadas = list(dic_cant_temporadas)
    list_n_temporadas = list(dic_cant_temporadas.values())
    print('@@@@@@')
    print(list_name_temporadas)
    print(list_n_temporadas)
    
    #vamos a crear una lista de listas para almacenar las temporadas
    

    matriz = []
    for name in list_name_temporadas:
        sub_list = [name]
        #for cant in list_n_temporadas:
        for i in range(list_n_temporadas[list_name_temporadas.index(name)]):
            sub_list.append(i+1)
        
        matriz.append(sub_list)
    
    print(matriz)


    ctx = Context({'matriz':matriz,'n_temporadas':dic_cant_temporadas,"consulta": algo, "papa":"padre"})
    documento = plt.render(ctx)

    return HttpResponse(documento)

def index(request, n_temporada):
    #se carga el template
    #doc_externo = open("C:/Users/Matias Briones/Desktop/t1_taller_integracion/Breakingbad/aplicaciones/templates/aplicaciones/temporadas.html")
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/index.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()


    ctx = Context({ "numero_temporada":n_temporada})
    documento = plt.render(ctx)

    return HttpResponse(documento)
