# Importando paquetes necesarios:
from fibonacci import fibo
from time import time
import multiprocessing
import sys

# Definiendo el main:
def main():

	# Inicializando vector en 33 para 144 cálculos:
	max_fibo = 33
	tam = 144 # Tamaño del vector (Número de Fibonaccis a calcular).
	vectorSeq = [max_fibo] * tam
	num_cpus = multiprocessing.cpu_count()
	
	# Calculando los valores Fibonacci y almacenando en el vector:
	print(f"Calculando el fibonacci {max_fibo} en {num_cpus} CPU's")
	ts = time()
	for x in range(tam):
		y = fibo(max_fibo)
		vectorSeq[x] = y
		print(f"El fibonacci de {max_fibo} es: {y}")

	# Imprimiendo tiempo de ejecución y el vector resultante:	
	print(f"Tomo {time() - ts}")
	print(f"El vector resultante es: {vectorSeq}")

if __name__ == "__main__":
  main()
