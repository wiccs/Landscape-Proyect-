import requests
from flask import render_template


class Conexion:

    def conectar(self,latitud,longitud):
        EARTHDATA_USERNAME = 'wiccs'
        EARTHDATA_PASSWORD = 'Sailorvenus1236.'

        # Llamada a la API de Earthdata para obtener los datos de Landsat
        landsat_url = f'https://api.nasa.gov/planetary/earth/imagery/?lat={latitud}&lon={longitud}&dim=0.01&api_key=DEMO_KEY'
        response = requests.get(landsat_url, auth=(EARTHDATA_USERNAME, EARTHDATA_PASSWORD))

        if response.status_code == 200:
            # Procesar los datos de Landsat y mostrar en una cuadrícula
            data = response.json()
            return data
        else:
            return f"Error en la solicitud: {response.status_code}"
