import requests


class Conexion:
    def conectar(self, latitud, longitud):
        apiKey = 'LHBV2N-6A3UNU-WTBWR8-5C36'
        url = f'https://api.n2yo.com/rest/v1/satellite/positions/39084/{latitud}/{longitud}/0/2000?apiKey={apiKey}'

        respuesta = requests.get(url)
        print('Cargando datos, por favor espere ...')

        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
        else:
            print(f"Error en la solicitud: {respuesta.status_code}")
            return None

    def datosGeograf(self,latitud, longitud):
        pointUser = [latitud,longitud]
        return pointUser