import datetime



def dic_temporadas(consulta):
    if len(consulta) != 0:
        
        #si la consulta no esta vacia
        serie_analizada = consulta[0]['series']
        temporada_analizada = int(consulta[0]['season'])
        dic_serie_temporadas = {serie_analizada:temporada_analizada}

        for cap in consulta:
            if cap['series'] == serie_analizada:
                if int(cap['season']) > temporada_analizada:
                    temporada_analizada = int(cap['season'])
                    dic_serie_temporadas[serie_analizada] = temporada_analizada

            else:
                #dic_serie_temporadas.update({serie_analizada:temporada_analizada})
                serie_analizada = cap['series']
                temporada_analizada = int(cap['season'])
                #print(serie_analizada)

        return dic_serie_temporadas

    
    #si la consulta viene vacia enviaremos un mensaje por consola
    else:
        print('LA CONSULTA VIENE VACIA')
        return {}



def lista_episodios(consulta, name_serie, n_temporada):
    
    list_episodio = []
    if len(consulta) != 0:
        
        for item in consulta:

            if item['series'] == name_serie and int(item['season']) == int(n_temporada):
                list_aux = [item['episode'],item['title'],item["episode_id"]]
                list_episodio.append(list_aux)

        return list_episodio

    
    #si la consulta viene vacia enviaremos un mensaje por consola
    else:
        print('LA CONSULTA VIENE VACIA')
        return ['paso x aqui, soy un error']


def list_info_cap(consulta):
    #list_webeo = ["esto deberia verso como un eror"]
    info_cap = []
    if len(consulta) != 0:
        print('\n\n\n')
        print(consulta)
        dic_consulta = consulta[0]
        info_cap.append(dic_consulta["title"])
        info_cap.append(dic_consulta["season"])
        info_cap.append(dic_consulta["episode"])
        #info_cap.append(dic_consulta["air_date"])
                 
        d = datetime.datetime.strptime(dic_consulta["air_date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        new_format = "d-m-Y"
        d.strftime(new_format)
        info_cap.append(d)


        info_cap.append(dic_consulta["characters"])

        return info_cap
        #return list_webeo


    
    #si la consulta viene vacia enviaremos un mensaje por consola
    else:
        print('LA CONSULTA VIENE VACIA')
        return ['paso x aqui, soy un error']


def matriz_personajes_buscados(consulta):


    matriz_info = []  
    '''
    INFO GUARDDA en la matriz EN ORDEN: 
    "name"
    "occupation"    
    "status"
    "nickname"
    "appearance"
    "portrayed"
    "category"
    "better_call_saul_appearance"
    "img"
    '''
    for dic_personaje in consulta:
        list_aux = [
            dic_personaje["name"],
            dic_personaje["occupation"],
            dic_personaje["status"],
            dic_personaje["nickname"],
            dic_personaje["appearance"],
            dic_personaje["portrayed"],
            dic_personaje["category"],
            dic_personaje["better_call_saul_appearance"],
            dic_personaje["img"]            
        ]
        matriz_info.append(list_aux)
    
    return matriz_info


   