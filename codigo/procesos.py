import array_queue as arr

class Procesos:

    def __init__(self, user_id, process_id,tipo,d_estimada,d_real,contador=0, tiempo_inicial = int()):
        self._user_id = user_id
        self._process_id = process_id
        self._tipo = tipo
        self._d_estimada = d_estimada
        self._d_real = d_real
        self._contador = contador
        self._tiempo_inicial = tiempo_inicial

        
    def __str__(self) -> str:
        return f'Contador: {self.contador}, {self.process_id}, {self.user_id}, {self.tipo}, {self.d_estimada}, d_real: {self.d_real}, d_inicial: {self.tiempo_inicial}'


    @property
    def user_id(self):
        return self._user_id
    

    @property
    def process_id(self):
        return self._process_id
    

    @property
    def tipo(self):
        return self._tipo


    @property
    def d_estimada(self):
        return self._d_estimada
    @d_estimada.setter
    def d_estimada(self, d_estimada):
        self._d_estimada = d_estimada

        
    @property
    def d_real(self):
        return int(self._d_real)
    @d_real.setter
    def d_real(self, d_real):
        self._d_real = d_real
        

    @property
    def contador(self):
        return self._contador
    @contador.setter
    def contador(self, contador):
        self._contador = contador


    @property
    def tiempo_inicial(self):
        return self._tiempo_inicial
    @tiempo_inicial.setter
    def tiempo_inicial(self, tiempo_inicial):
        self._tiempo_inicial = tiempo_inicial
