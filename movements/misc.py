import requests
from flask import request

API_KEY = '19780f44'

def llamada_api():
    lista_pelis = []
    error = ''
    titulo = request.form['pelicula']    
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={titulo}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == 'False':
            error = datos['Error']
            return error
        else:
            for elemento in datos['Search']:
                if elemento['Type'] == 'movie':
                    if elemento['Title'] not in lista_pelis:
                        lista_pelis.append(elemento['Title'])
            return lista_pelis
    else:
        error = respuesta.status_code
        if error == 401:
            return "Error en la autentificación (Comprueba tu API_KEY)"

def llamada_api2():
    titulo = request.form['select']
    film_selected = []
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={titulo}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        nuevos_datos = respuesta.json()
        if nuevos_datos['Response'] == 'False':
            error = nuevos_datos['Error']
            return error
        else:
            for elemento in nuevos_datos['Search']:
                if elemento['Title'] == titulo:
                    if elemento['Poster'] == 'N/A':
                        elemento['Poster'] = 'http://barracamalvin.com/addons/default/themes/sl/img/image-not-found.png'
                    film_selected.append(elemento)
            return film_selected
    else:
        error = respuesta.status_code
        if error == 401:
            return "Error en la autentificación (Comprueba tu API_KEY)"
