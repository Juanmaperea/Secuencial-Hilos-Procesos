#
# Este script calcula de manera secuencial el Fibonacci 
# serie de Fibonacci.
#
# Autor: Juan Manuel Perea - juan.coronado@correounivalle.edu.co
# Fecha: 2024-10-16
#
from fibonacci import fibo
from time import time
import multiprocessing
import sys
import os

def main():

	# Inicializando vector en 33 para 144 cálculos:
	max_fibo = 33
	tam = 10 # Tamaño del vector (Número de Fibonaccis calculados).
	vectorSeq = [max_fibo] * tam
	num_cpus = multiprocessing.cpu_count()
	
	# Calculando los valores Fibonacci y almacenando en el vector:
	print(f"Calculando el fibonacci {max_fibo} en {num_cpus} CPUs")
	ts = time()
	for x in range(tam):
		y = fibo(max_fibo)
		vectorSeq[x] = y
		print(f"El fibonacci de {max_fibo} es: {y}")

	# Imprimiendo tiempo de ejecución:	
	print(f"Tomo {time() - ts}")

if __name__ == "__main__":
  main()
