from movements import app
import requests
import config # Modulo config importado de forma no me bien vista

from flask import render_template, request, url_for, redirect



@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        lista_pelis = []
        error = ''
        titulo = request.form['pelicula']
        API_KEY = '19780f44'
        url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={titulo}'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos['Response'] == 'False':
                error = datos['Error']
            else:
                for elemento in datos['Search']:
                    if elemento['Type'] == 'movie':
                        lista_pelis.append(elemento['Title'])
        else:
            error = respuesta.status_code

        return render_template('opciones.html', datos=lista_pelis, error=error)

    return render_template('index.html')

@app.route('/muestrapeli', methods=['GET', 'POST'])
def mostrarpelicula():
    titulo = request.form['select']
    API_KEY = '19780f44'
    film_selected = []
    url = f'http://www.omdbapi.com/?apikey={API_KEY}&s={titulo}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        nuevos_datos = respuesta.json()
        if nuevos_datos['Response'] == 'False':
            error = nuevos_datos['Error']
        else:
            for elemento in nuevos_datos['Search']:
                if elemento['Title'] == titulo:
                    film_selected.append(elemento)
    else:
        error = respuesta.status_code

    return render_template('pelicula.html', pelicula=film_selected[0])
