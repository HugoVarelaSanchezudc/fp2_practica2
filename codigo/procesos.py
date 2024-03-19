import array_queue as arr

class Procesos:

    def __init__(self, user_id, process_id, tipo, d_estimada, d_real):
        self._user_id = user_id
        self._process_id = process_id
        self._tipo = tipo
        self._d_estimada = d_estimada
        self._d_real = d_real


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
    @d_estimada.settter
    def d_estimada(self, d_estimada):
        self._d_estimada = d_estimada

        
    @property
    def d_real(self):
        return self._d_real
    @d_real.settter
    def d_real(self, d_real):
        self._d_real = d_real



class GPU (Procesos):
    def __init__(self, user_id, process_id, tipo, d_estimada, d_real):

        super().__init__(user_id, process_id, tipo, d_estimada, d_real)
        

class CPU (Procesos):
    def __init__(self, user_id, process_id, tipo, d_estimada, d_real):

        super().__init__(user_id, process_id, tipo, d_estimada, d_real)
        
