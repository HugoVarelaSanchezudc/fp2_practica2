import array_queue as aq
from procesos import *
import sys

archivo = sys.argv[1]

gestor_cola_cpu = aq.ArrayQueue()
gestor_cola_gpu = aq.ArrayQueue()

with open(archivo,'r') as contenido:
    info_procesos = contenido.read()

for line in info_procesos.split('\n'):
    if len(line) != 0:
        if line.split(' ')[2] == 'cpu':
            user_id, process_id, tipo, d_estimada, d_real = line.split(' ')[1],line.split(' ')[0], line.split(' ')[2], line.split(' ')[3], line.split(' ')[4]
            gestor_cola_cpu.enqueue(aq.CPU(line))
        else:
            gestor_cola_gpu.enqueue(aq.GPU(line))
