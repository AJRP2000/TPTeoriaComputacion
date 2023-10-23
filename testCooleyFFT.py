import numpy as np
import time

def cooley_tukey_fft(tren_de_impulso):
    N = len(tren_de_impulso)

    # Validar si N es una potencia de 2
    if not (N & (N - 1) == 0) and N > 0:
        # Calcular la siguiente potencia de 2 mas cercana a la longitud del tren de impulso
        padded_N = 2 ** (N - 1).bit_length()
        
        # Agregar los espacios entre el array recibido para tener una longitud igual a una potencia de 2 y 
        # Llenar los nuevos espacios con 0
        tren_de_impulso = np.pad(tren_de_impulso, (0, padded_N - N), 'constant')

    if N <= 1:
        return tren_de_impulso #Caso Base
    else:
        par = cooley_tukey_fft(tren_de_impulso[0::2]) #Iterar de forma recursiva los pares
        impar = cooley_tukey_fft(tren_de_impulso[1::2]) #Iterar de forma recursiva los impares
        resultado = []
        for k in range(N//2):
            twiddle = np.exp(-2j * np.pi * k / N) * impar[k] #Calcular el valor impar tomando en cuenta el valor de euler externo
            resultado.append(par[k] + twiddle) 
            resultado.append(par[k] - twiddle)
            
        return resultado


def test():
    tiempo_entre_puntos = 1
    magnitud_prueba = 1
    cantidad_puntos_prueba = 3**1
    data = np.zeros(cantidad_puntos_prueba)
    data[::tiempo_entre_puntos] = magnitud_prueba

    # Calcular la FFT
    tiempo_inicio = time.time()
    resultado = cooley_tukey_fft(data)
    tiempo_fin = time.time()
    duracion_funcion = tiempo_fin - tiempo_inicio

    # Print el tiempo elapsado
    print("Tiempo de la transformada en segundos: " + str(duracion_funcion))
    #print("Resultado de la transformada:")
    #print(resultado)
    