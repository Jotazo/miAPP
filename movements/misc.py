import requests
from flask import request
from config import API_KEY

def llamada_api_general(tipo_busqueda=''):
    peliculas = []
    error = ''
    titulo = request.form[tipo_busqueda]    
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={titulo}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == 'False':
            error = datos['Error']
            return error
        else:
            if tipo_busqueda == 'pelicula':
                for elemento in datos['Search']:
                    if elemento['Type'] == 'movie':
                        if elemento['Title'] not in datos:
                            peliculas.append(elemento['Title'])
                return peliculas
            else:
                for elemento in datos['Search']:
                    if elemento['Title'] == titulo:
                        if elemento['Poster'] == 'N/A':
                            elemento['Poster'] = 'http://barracamalvin.com/addons/default/themes/sl/img/image-not-found.png'
                        peliculas.append(elemento)
                return peliculas
    else:
        error = respuesta.status_code
        if error == 401:
            return "Error en la autentificación (Comprueba tu API_KEY)"