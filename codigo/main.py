import array_queue as aq
from procesos import *
import sys




class Gestor_Colas:
    
    def __init__(self,proceso):
        self._proceso = proceso


    def __str__ (self):
        return f'{self.proceso}'
        

    @property
    def proceso(self):
        return self._proceso
    
    def is_penalitated(self, proceso,index, usuarios=[]):
        if (index == 1) or (index == 3):
            tiempo_ejec = proceso.contador - proceso.tiempo_inicial
            if (tiempo_ejec > 5) and (proceso.user_id not in usuarios):
                usuarios.append(proceso.user_id)
                print(f'{proceso.user_id} ha sido penalizado')
        


    def tipo_cola(self,colas):
        
        i = self.proceso
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
    
contador = 0

#Creamos un for, dondem metemos cada linea de codigo de longitud distinta de 0 en la cola

for line in info_procesos.split('\n'):

    if len(line) != 0:

        datos_proceso = line.split()
        proces_id, user_id, tipo1, dur_estimada, dur_real = datos_proceso
        proceso1=Procesos(proces_id, user_id, tipo1, dur_estimada, dur_real,contador)

        cola_reg.enqueue(proceso1)



usuarios_penalizados = []

while len(cola_reg) > 0:
    aux1 = cola_reg.dequeue()
    aux1.tiempo_inicial = contador
    aux1.contador = contador
    
    proceso = Gestor_Colas(aux1)
    proceso.tipo_cola(colas)
    
    
    # print('Usario\n',aux1.user_id,'\n\n')
    # print('Tipo',aux1.d_estimada)
    
    # print(usuarios_penalizados)
    
    nombre = aux1.user_id
    
    if nombre in usuarios_penalizados:
        if (aux1.tipo == 'gpu') and (aux1.d_estimada == 'short'):
            aux1.d_estimada = 'long'
            cola_reg.enqueue(gpu_short.dequeue())
            usuarios_penalizados.pop(usuarios_penalizados.index(aux1.user_id))
            print(f'Movemos {aux1.process_id} de {nombre} al final de la cola de gpu')
        elif (aux1.tipo == 'cpu') and (aux1.d_estimada == 'short'):
            aux1.d_estimada = 'long'
            cola_reg.enqueue(cpu_short.dequeue())
            usuarios_penalizados.pop(usuarios_penalizados.index(aux1.user_id))
            print(f'Movemos {aux1.process_id} de {nombre} al final de la cola de gpu')
    else:
    
        if len(gpu_short) > 0:
            index = 1
        elif len(cpu_short) > 0:
            index = 3
        elif len(gpu_long) > 0:
            index = 0
        else:
            index = 2
            
        for i in range(aux1.d_real):
            contador += 1
    
        
        aux1.contador = contador
        
        print(aux1)
        
        proceso.is_penalitated(aux1,index, usuarios_penalizados)
        
        colas[index].dequeue()

    
    
    
   
        

    
'''
    print('cpu short', len(cpu_short))
    print('cpu long', len(cpu_long))
    print('gpu short', len(gpu_short))
    print('gpu long', len(gpu_long))

#H: pq no se mira ya la penalizacion antes de guardarlo, ya que al meterlo al tipo cola puede meter un proceso
#que por la penalizacion iria en una cola distinta

    
        
print('CPU Short\n\n\n', cpu_short)
print('CPU Long\n\n\n', cpu_long)
print('GPU Short\n\n\n', gpu_short)
print('GPU Long\n\n\n', gpu_long)
'''










'''
#Pruebas

print(cola_reg)
procesos = Gestor_Colas(cola_reg) #Creo el gestor de colas
print(procesos)
procesos.tipo_cola(colas) #Asocio cada proceso de la cola de de registros segun su tipo y duracion en 4 colas diferentes

print('Hola', cpu_short)'''


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
