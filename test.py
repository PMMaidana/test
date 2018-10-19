class Llamada:
    def __init__(self, fecha_inicio, fecha_fin, telefono, cliente):
        self.fechaI = fecha_inicio
        self.fechaF = fecha_fin
        self.tel = telefono
        self.cliente0 = cliente

    def llamada_international(self):
        print((self.fechaF - self.fechaI) * 1.25)

    def llamada_national(self):
        print((self.fechaF - self.fechaI) * 0.75)

    def llamada_interstate(self):
        print((self.fechaF - self.fechaI) * 0.5)

