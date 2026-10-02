TIPOS_PERMITIDOS = ("carro", "moto", "bicicleta")

TARIFAS = {
    "carro": 3000,
    "moto": 1500,
    "bicicleta": 500,
}


def calcular_cobro(tipo, horas, descuento=0):
    horas_cobradas = horas if horas >= 1 else 1
    valor = TARIFAS[tipo] * horas_cobradas
    return int(valor - valor * descuento / 100)


def placa_valida(placa):
    return len(placa) == 6


class Parqueadero:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []
        self.historial = []

    def ingresar(self, placa, tipo, conductor):
        if len(self.vehiculos) >= self.capacidad:
            return "El parqueadero esta lleno"
        if tipo not in TIPOS_PERMITIDOS:
            return f"Tipo no permitido: {tipo}"
        if not placa_valida(placa):
            return "La placa debe tener 6 caracteres"
        if any(v["placa"] == placa for v in self.vehiculos):
            return f"El vehiculo {placa} ya esta adentro"

        self.vehiculos.append({"placa": placa, "tipo": tipo, "conductor": conductor})
        return f"Vehiculo {placa} ingresado"

    def salir(self, placa, horas, descuento=0):
        for vehiculo in self.vehiculos:
            if vehiculo["placa"] == placa:
                valor = calcular_cobro(vehiculo["tipo"], horas, descuento)
                self.vehiculos.remove(vehiculo)
                self.historial.append(
                    (vehiculo["placa"], vehiculo["tipo"], horas, valor)
                )
                return f"Vehiculo {placa} salio. Pago: {valor}"

        return f"El vehiculo {placa} no esta adentro"

    def placas_adentro(self):
        return [v["placa"] for v in self.vehiculos]

    def total_recaudado(self):
        return sum(registro[3] for registro in self.historial)

    def reporte_por_tipo(self):
        reporte = {}
        for _, tipo, _, valor in self.historial:
            reporte[tipo] = reporte.get(tipo, 0) + valor
        return reporte


if __name__ == "__main__":
    parqueadero = Parqueadero(capacidad=2)

    print(parqueadero.ingresar("ABC123", "carro", "Carlos"))
    print(parqueadero.ingresar("XYZ789", "moto", "Ana"))
    print(parqueadero.ingresar("QW12", "carro", "Luis"))
    print(parqueadero.ingresar("ABC123", "bicicleta", "Mia"))

    print("Adentro:", parqueadero.placas_adentro())

    print(parqueadero.salir("ABC123", 3))
    print(parqueadero.salir("XYZ789", 2, 10))

    print("Total recaudado:", parqueadero.total_recaudado())
    print("Por tipo:", parqueadero.reporte_por_tipo())