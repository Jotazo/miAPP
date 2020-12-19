from movements import app
from movements import misc

import requests
import config # Modulo config importado de forma no bien vista

from flask import render_template, request, url_for, redirect

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        
        datos = misc.llamada_api()
        
        if isinstance(datos, str):
            return render_template('index.html', errores=datos)

        return render_template('index.html', datos=datos)

    return render_template('index.html')

@app.route('/muestrapeli', methods=['GET', 'POST'])
def mostrarpelicula():
    film_selected = misc.llamada_api2()

    return render_template('pelicula.html', pelicula=film_selected[0])
