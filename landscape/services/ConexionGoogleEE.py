import ee

class Conexion:
    def conectar(self):
            ee.Authenticate()
            ee.Initialize(project='august-bucksaw-315705')

