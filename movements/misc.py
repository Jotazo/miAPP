import requests
from flask import request
from config import API_KEY

validos = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Plot', 'Poster']

def llamada_api_general(tipo_busqueda='', param_url='s'):
    peliculas = []
    error = ''
    titulo = request.form[tipo_busqueda]    
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&{param_url}={titulo}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == 'False':
            if datos['Error'] == 'Incorrect IMDb ID.':
                error = 'Empty field'
            else:
                error = datos['Error']
            return error
        else:
            if tipo_busqueda == 'pelicula':
                for elemento in datos['Search']:
                    if elemento['Type'] == 'movie':
                        d = {'Title':elemento['Title'], 'imdb':elemento['imdbID']}    
                        peliculas.append(d)
                return peliculas
            else:
                l = {}
                for k, v in datos.items(): 
                    if k in validos and k not in l:
                        l[k] = v
                        
                for k, v in l.items():
                    if v == 'N/A' and k != 'Poster':
                        l[k] = '--No Results--'
                    elif v == 'N/A' and k == 'Poster':
                        l[k] = 'http://barracamalvin.com/addons/default/themes/sl/img/image-not-found.png'

                return l
    else:
        error = respuesta.status_code
        if error == 401:
            return "Error en la autentificación (Comprueba tu API_KEY)"