
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



