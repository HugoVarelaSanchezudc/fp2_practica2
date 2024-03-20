import array_queue as arr

class Procesos:

    def __init__(self,process_id : str, user_id,tipo : str, d_estimada : int, d_real : int,interaccion = 0, tiempo_inicial = int()):
        self._user_id = user_id
        self._process_id = process_id
        self._tipo = tipo
        self._d_estimada = d_estimada
        self._d_real = d_real
        self._interaccion = interaccion
        self._tiempo_inicial = tiempo_inicial

        
    def __str__(self) -> str:
        return f'{self.process_id}, {self.user_id}, {self.tipo}, {self.d_estimada}, interaccion: {self.interaccion}, d_inicial: {self.tiempo_inicial}, d_real: {self.d_real}'


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
    def interaccion(self):
        return self._interaccion
    @interaccion.setter
    def interaccion(self, interaccion):
        self._interaccion = interaccion


    @property
    def tiempo_inicial(self):
        return self._tiempo_inicial
    @tiempo_inicial.setter
    def tiempo_inicial(self, tiempo_inicial):
        self._tiempo_inicial = tiempo_inicial
