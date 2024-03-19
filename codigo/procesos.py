import array_queue as arr

class Procesos:

    def __init__(self, user_id, process_id,tipo,d_estimada,d_real):
        self._user_id = user_id
        self._process_id = process_id
        self._tipo = tipo
        self._d_estimada = d_estimada
        self._d_real = d_real

    def __str__(self) -> str:
        return f'{self.process_id}, {self.user_id}, {self.tipo}, {self.d_estimada}, {self.d_real}'

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
        return self._d_real
    @d_real.setter
    def d_real(self, d_real):
        self._d_real = d_real
