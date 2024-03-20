import array_queue as aq
from procesos import *
import sys
import time



class Gestor_Colas:
    
    def __init__(self,proceso):
        self._proceso = proceso


    def __str__ (self):
        return f'{self.proceso}'
        

    @property
    def proceso(self):
        return self._proceso
    

    #Comprobar cosas


    def is_penalitated(self, proceso, usuarios):
            
            tiempo_ejec = proceso.interaccion - proceso.tiempo_inicial
            print(tiempo_ejec)
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






def penalizar(usuarios_penalizados, cola, colas):
    aux = cola.first()
    nombre = aux.user_id
    print ('si')
    if nombre in usuarios_penalizados:

        if aux.tipo == 'gpu':
            print(' a gpu long')
            colas[0].enqueue(cola.dequeue())
            usuarios_penalizados.pop(usuarios_penalizados.index(aux.user_id))

            print(f'Movemos {aux.process_id} de {nombre} al final de la cola de gpu')

            

        elif aux.tipo == 'cpu':
            
            print(' a cpu long')
            
            colas[2].enqueue(cola.dequeue())
            usuarios_penalizados.pop(usuarios_penalizados.index(aux.user_id))

            print(f'Movemos {aux.process_id} de {nombre} al final de la cola de cpu')





def ejecucion (cola, usu_penalizados, contador,colas):
    aux = cola.first()
    proceso = Gestor_Colas(aux)
    
    if aux.tiempo_inicial == None:
        aux.tiempo_inicial = contador
        aux.interaccion = contador
        if aux.tipo == 'short':
             print('\n\n\n------------------------\n\n\n\n\n')
             penalizar(usu_penalizados, cola,colas)
    
    else:

        if aux.d_real == (contador - aux.tiempo_inicial):
            print(f'{aux.tiempo_inicial}\n\n\n\n')
            if aux.d_estimada == 'short' :
                # print('siuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
                proceso.is_penalitated(aux, usu_penalizados)
            cola.dequeue()

        else:
            aux.interaccion = contador
    





def main():

    #archivo = sys.argv[1]
    archivo = 'processes0.txt'


    cola_reg= aq.ArrayQueue()
    gpu_short = aq.ArrayQueue()
    gpu_long = aq.ArrayQueue()
    cpu_short = aq.ArrayQueue()
    cpu_long = aq.ArrayQueue()


    colas = (gpu_long,gpu_short,cpu_long,cpu_short)
    usuarios_penalizados = []
    contador = 0

    with open(archivo, 'r') as contenido:
        info_procesos = contenido.read()


    #Creamos un for, dondem metemos cada linea de codigo de longitud distinta de 0 en la cola

    for line in info_procesos.split('\n'):
        
        if len(line) != 0:

            datos_proceso = line.split()
            proces_id, user_id, tipo1, dur_estimada, dur_real = datos_proceso
            proceso1 = Procesos(proces_id, user_id, tipo1, dur_estimada, dur_real)

            cola_reg.enqueue(proceso1)



    while ((len(cola_reg) != 0) or ((len(cpu_long) + len(cpu_short) + len(gpu_long) + len(gpu_short)) > 0)):    
        if not(len(cola_reg) == 0):
            proceso_actual = cola_reg.dequeue()
        #proceso_actual.tiempo_inicial = contador
        # if proceso_actual.tipo == 'gpu' and proceso_actual.d_estimada == 'long':
        #     print('METEMOS UN {proceso_actual.tipo}, {proceso_actual.d_estimada}')
        
        print(f'METEMOS UN {proceso_actual.tipo}, {proceso_actual.d_estimada}')

        proceso = Gestor_Colas(proceso_actual)
        proceso.tipo_cola(colas)
        
        


        if len(cpu_short) > 0:
            ejecucion(cpu_short, usuarios_penalizados, contador,colas)
            print(f'\n\n\n CPU Short: {contador}', cpu_short)
            # print(f'\n y su longitud: {len(cpu_short)}')
            time.sleep(1.5)
        if len(gpu_short) > 0:
            ejecucion(gpu_short, usuarios_penalizados, contador,colas)
            print(f'\n\n\n GPU Short: {contador}', gpu_short)
            # print(f'\n y su longitud: {len(gpu_short)}')
            time.sleep(1.5)
        if len(cpu_long):
            ejecucion(cpu_long, usuarios_penalizados, contador,colas)
            print(f'\n\n\n CPU Long: {contador}', cpu_long)
            # print(f'\n y su longitud: {len(cpu_long)}')
            time.sleep(1.5)
        if len(gpu_long):
            ejecucion(gpu_long, usuarios_penalizados, contador, colas)
            print(f'\n\n\n GPU Long: {contador}', gpu_long)
            # print(f'\n y su longitud: {len(gpu_long)}')
            # time.sleep(2)



        contador += 1



if __name__ == '__main__':
    main()










    