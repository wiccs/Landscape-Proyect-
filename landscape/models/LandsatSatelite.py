import json
from typing import List

class Info:
    #constructor para info
    def __init__(self, satname: str, satid: int, transactionscount: int):
        self.satname = satname
        self.satid = satid
        self.transactionscount = transactionscount

#repr es un metodo similar a java para cuando debemos imprimir arreglos.
    def __repr__(self):
        #la f es para poder formatear cadenas es decir insertar variables en las cadenas con {}.
        return f"Info(satname='{self.satname}', satid={self.satid}, transactionscount={self.transactionscount})"


#Otra clase
class Position:
    #constructor
    def __init__(self, satlatitude: float, satlongitude: float, sataltitude: float,
                 azimuth: float, elevation: float, ra: float, dec: float,
                 timestamp: int, eclipsed: bool):
        self.satlatitude = satlatitude
        self.satlongitude = satlongitude
        self.sataltitude = sataltitude
        self.azimuth = azimuth
        self.elevation = elevation
        self.ra = ra
        self.dec = dec
        self.timestamp = timestamp
        self.eclipsed = eclipsed

        self.arregloPuntos = [self.satlatitude,self.satlongitude]

    def imprimirPuntos(self):
            print(self.arregloPuntos)

    def __repr__(self):
        return (f"Position(satlatitude={self.satlatitude}, satlongitude={self.satlongitude}, "
                f"sataltitude={self.sataltitude}, azimuth={self.azimuth}, elevation={self.elevation}, "
                f"ra={self.ra}, dec={self.dec}, timestamp={self.timestamp}, eclipsed={self.eclipsed})")





#Este constructor se encarga de guardar los datos del satelite y guarda las posiciones como una lista
class SatelliteData:
    def __init__(self, info: Info, positions: List[Position]):
        self.info = info
        self.positions = positions

    def __repr__(self):
        return f"SatelliteData(info={self.info}, positions={self.positions})"
