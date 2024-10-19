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

def main():
	vectorF = []
	ts = time()
	for x in range(144):
		y = fibo(33)
		print(f"y: {y}")
		vectorF.append(y)
	print(f"El fibonacci es {y}")
	print(f"Tomo {time() - ts}")


if __name__ == "__main__":
  main()
