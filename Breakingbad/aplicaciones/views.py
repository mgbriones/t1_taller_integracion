from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.template import Context, Template


#modulos creados
from aplicaciones.funciones_temporada import dic_temporadas, lista_episodios, list_info_cap, matriz_personajes_buscados




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
        #print('\n\n@@@@@@@@@@@@@@@@@@@@@@@')
        #print(content)
        #print(content[0])
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

def index(request,name_serie, n_temporada):
    #se carga el template
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/index.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()


    #ahora necesitamos la funcion que haga la peticion y entrege una lista
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes'
    algo = api(url)

    matriz_episodios = lista_episodios(algo, name_serie, n_temporada) #aqui va una funcion, lol


    ctx = Context({ "name_serie":name_serie,"numero_temporada":n_temporada, "matriz_episodios":matriz_episodios})
    documento = plt.render(ctx)

    return HttpResponse(documento)


def capitulo(request, id_capitulo):
    #se carga el template
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/capitulo.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()


    #ahora necesitamos la funcion que haga la peticion y entrege una lista
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(id_capitulo)
    algo = api(url)

    matriz_info = list_info_cap(algo)

    ctx = Context({"matriz_info":matriz_info})
    documento = plt.render(ctx)

    return HttpResponse(documento)


def personaje(request, name_personaje):
    #se carga el template
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/personaje.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()


    #ahora necesitamos la funcion que haga la peticion y entrege una lista
    #url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(id_capitulo)
    #algo = api(url)

    #matriz_info = list_info_cap(algo)

    
    

    nombre_a_buscar = name_personaje.replace(" ","+")
    url_2 = "https://tarea-1-breaking-bad.herokuapp.com/api/characters?name="+nombre_a_buscar

    consulta_2 = api(url_2)
    resultado_consulta = consulta_2[0]

    print("\n\n\n\n@@@@@@@@@2")
    print(resultado_consulta)
    print("\n\n\n@@@@@@@@@@@@@@@@@@@")
    print(consulta_2)

    ctx = Context({"mensaje":"TODO BIEN AUN", "name_personaje":name_personaje,
     "resultado_consulta":resultado_consulta,
     "name":resultado_consulta["name"],
     "occupation":resultado_consulta["occupation"],
     "img":resultado_consulta["img"],
     "status":resultado_consulta["status"],
     "nickname":resultado_consulta["nickname"],
     "appearance":resultado_consulta["appearance"],
     "portrayed":resultado_consulta["portrayed"],
     "category":resultado_consulta["category"],
     "better_call_saul_appearance":resultado_consulta["better_call_saul_appearance"],
     
     })
    documento = plt.render(ctx)

    return HttpResponse(documento)



def busqueda(request):
     #se carga el template
    doc_externo = open("../Breakingbad/aplicaciones/templates/aplicaciones/busqueda.html")
    plt = Template(doc_externo.read()) #se lee el template
    doc_externo.close()

    mensaje = request.GET["busq"]

    resultado_consulta = []


    id = 0
    while True:   #esta linea  puede que tenga que borrarla

        url = "https://tarea-1-breaking-bad.herokuapp.com/api/characters?name="+str(mensaje)+"&limit=10&offset="+str(id)
        consulta = api(url)  # esto es una lista
        if len(consulta)!= 0:
            #resultado_consulta.append(consulta)
            resultado_consulta += consulta
            id += 10
        
        else: #la lista esta vacia
            break

    
    matriz_info = matriz_personajes_buscados(resultado_consulta)

    

    ctx = Context({"info":matriz_info})
    documento = plt.render(ctx)

    return HttpResponse(documento)