import numpy as np
import time

def dft_separando_pares_impares(tren_de_impulso):
    N = len(tren_de_impulso)
    transformada_fourier = np.zeros(N, dtype=complex)
    
    for k in range(N):
        euler_externo = np.exp(-2j * np.pi/N * k)
        for n in range(N//2):
            euler_interno = np.exp(-2j * np.pi/N * k * 2*n)
            parte_par = tren_de_impulso[2*n] *      euler_interno
            parte_impar = tren_de_impulso[2*n+1] *  euler_interno
            transformada_fourier[k] += parte_par +  euler_externo * parte_impar
    return transformada_fourier

def test():
    # Example data
    tiempo_entre_puntos = 1
    magnitud_prueba = 1
    cantidad_puntos_prueba = 16**3
    data = np.zeros(cantidad_puntos_prueba)
    data[::tiempo_entre_puntos] = magnitud_prueba

    # Calculate the DFT
    tiempo_inicio = time.time()
    resultado = dft_separando_pares_impares(data)
    tiempo_fin = time.time()
    duracion_funcion = tiempo_fin - tiempo_inicio

    # Print the resultado
    print("Tiempo de la transformada en segundos: " + str(duracion_funcion))
    #print("Resultado de la transformada:")
    #print(resultado)