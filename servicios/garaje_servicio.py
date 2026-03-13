# servicios/garaje_servicio.py

class GarajeServicio:
    def __init__(self):
        # Lista privada para almacenar los objetos Vehiculo
        self._vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self._vehiculos
    