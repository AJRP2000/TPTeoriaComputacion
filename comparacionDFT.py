import time
import numpy as np
from testCooleyFFT import cooley_tukey_fft
from testManual import manual_dft
from testParImpar import dft_separando_pares_impares
from testParImparComplejo import dft_complejo_pares_impares


# Data de Ejemplo
TIEMPO_ENTRE_IMPULSOS = 1
MAGNITUD_TREN = 1
CANTIDAD_DE_PUNTOS = 2**12
data = np.zeros(CANTIDAD_DE_PUNTOS)
data[::TIEMPO_ENTRE_IMPULSOS] = MAGNITUD_TREN

tiempo_inicio = time.time()
resultado_manual = manual_dft(data)
tiempo_fin = time.time()
duracion_funcion = tiempo_fin - tiempo_inicio
print("Tiempo elapsado en segundos para dft manual: " + str(duracion_funcion))

tiempo_inicio = time.time()
resultado_par_impar = dft_separando_pares_impares(data)
tiempo_fin = time.time()
duracion_funcion = tiempo_fin - tiempo_inicio
print("Tiempo elapsado en segundos para dft separando pares e impares: " + str(duracion_funcion))

tiempo_inicio = time.time()
resultado_par_impar_complejo = dft_complejo_pares_impares(data)
tiempo_fin = time.time()
duracion_funcion = tiempo_fin - tiempo_inicio
print("Tiempo elapsado en segundos para dft usando separacion compleja de pares e impares: " + str(duracion_funcion))

tiempo_inicio = time.time()
resultado_cooley = cooley_tukey_fft(data)
tiempo_fin = time.time()
duracion_funcion = tiempo_fin - tiempo_inicio
print("Tiempo elapsado en segundos para dft usando el metodo recursivo de Cooley Tukey: " + str(duracion_funcion))

#print(np.fft.fft(data))
#print("//////////////////////////////////////////")
#print(resultado_manual)
#print("//////////////////////////////////////////")
#print(resultado_par_impar)
#print("//////////////////////////////////////////")
#print(resultado_par_impar_complejo)
#print("//////////////////////////////////////////")
#print(resultado_cooley)