import array_queue as aq
from procesos import *
import sys




class Gestor_Colas:
    def __init__(self,cola_procesos):
        self._cola_procesos = cola_procesos

    def __str__ (self):
        return f'{self.cola_procesos}'
        

    @property
    def cola_procesos(self):
        return self._cola_procesos
    
    
    def tipo_cola(self,colas):
        while self.cola_procesos.__len__() > 0:

            i = self.cola_procesos.dequeue()
            # print(i.tipo)

            if i.tipo == 'cpu':

                if i.d_estimada == 'short':
                    colas[3].enqueue(i)

                else:
                    colas[2].enqueue(i)

            else:

                if i.d_estimada == 'short':
                    colas[1].enqueue(i)

                else:
                    colas[0].enqueue(i)
            

archivo = sys.argv[1]
cola_reg= aq.ArrayQueue()
gpu_short = aq.ArrayQueue()
gpu_long = aq.ArrayQueue()
cpu_short = aq.ArrayQueue()
cpu_long = aq.ArrayQueue()


colas = (gpu_long,gpu_short,cpu_long,cpu_short)


with open(archivo, 'r') as contenido:
    info_procesos = contenido.read()

for line in info_procesos.split('\n'):

    if len(line) != 0:

        datos_proceso = line.split()
        proces_id, user_id, tipo1, dur_estimada, dur_real = datos_proceso

        proceso1=Procesos(proces_id, user_id, tipo1, dur_estimada, dur_real)
        #print(proceso1)
        cola_reg.enqueue(proceso1)
    


#Pruebas

print(cola_reg)
procesos = Gestor_Colas(cola_reg) #Creo el gestor de colas
procesos.tipo_cola(colas) #Asocio cada proceso de la cola de de registros segun su tipo y duracion en 4 colas diferentes

print('Hola', cpu_short)


#-------------------------------------------------------------------Pruebas--------------------------------------------------------------------------



# print(cola_reg.__len__()) #Veo el tamaño total para luego comprobar que no hay perdidas

# print(gpu_long.__len__(),gpu_short.__len__(),cpu_long.__len__(),cpu_short.__len__()) #Imprimo el tamaño de cada uno para comprobar que no hubo perdidas

# #Imprimo el tipo y la duracion estimada de cada cola para comproabar que todo fue bien y no se "traspapeló nada"
# while gpu_long.__len__() > 0:
#     i = gpu_long.dequeue()
#     print (i.tipo, i.d_estimada) 
    
# while gpu_short.__len__() > 0:
#     i = gpu_short.dequeue()
#     print (i.tipo, i.d_estimada) 

# while cpu_long.__len__() > 0:
#     i = cpu_long.dequeue()
#     print (i.tipo, i.d_estimada) 
    
# while cpu_short.__len__() > 0:
#     i = cpu_short.dequeue()
#     print (i.tipo, i.d_estimada) 

