# Importando paquetes necesarios:
from threading import Thread
from fibonacci import fibo
from time import time
import multiprocessing
import sys

# Definiendo clase FibWorker, de donde se heredan las características de Thread para la ejecución:
class FiboWorker(Thread):
  def __init__(self, n, tid, vec):
    Thread.__init__(self)
    self.n = n
    self.tid = tid
    self.vec = vec

# Definiendo la actividad a ejecutar (Calcular el Fibonacci):
  def run(self):
    for z in range(12):
      self.vec[z] = fibo(self.vec[z])
      print(f"[{self.tid}] Fibonacci de {self.n} es {self.vec[z]}")

# Definiendo el main:
def main():

  # Inicializando vector en 33 para 144 cálculos:
  max_fibo = 33
  tam = 144 # Tamaño del vector (Número de Fibonaccis a calcular)
  vectorCon = [max_fibo] * tam
  if len(sys.argv) != 1:
    max_fibo = int(sys.argv[1])

  # Inicializando vector con trabajadores:  
  num_cpus = multiprocessing.cpu_count() # CPUs disponibles
  trabajadores = []
  print(f"Calculando el fibonacci {max_fibo} en {num_cpus} CPU's")

  # Asignando CPU's y relacionándolas con segmentos del vector:
  ts = time() # se toma tiempo 
  for x in range(num_cpus): # Ciclo para crear trabajadores
    print(f"Trabajador {x} comienza")
    worker = FiboWorker(max_fibo, x, vectorCon[(x * 12): (x * 12 + 12)])
    worker.start()
    trabajadores.append(worker)

# Ciclo para esperar a que las CPU's:
  for x in range(num_cpus): # Ciclo para esperar por trabajadores
    print(f"Esperando por trabajador {x}")
    trabajadores[x].join()
    vectorCon[(x * 12): (x * 12 + 12)] = trabajadores[x].vec
    
# Imprimiento tiempo y el vector:
  print(f"Tomo {time() - ts}")
  print(f"El vector resultante es: {vectorCon}")

if __name__ == "__main__":
  main()
