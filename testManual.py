import numpy as np
import time

def manual_dft(tren_de_impulso):
    N = len(tren_de_impulso)
    transformada_fourier = np.zeros(N, dtype=complex)
    
    for k in range(N):
        for n in range(N):
            transformada_fourier[k] += tren_de_impulso[n] * np.exp(-2j * np.pi/N * k * n)
    
    return transformada_fourier

# Example data
def test():
    tiempo_entre_puntos = 1
    magnitud_prueba = 1
    cantidad_puntos_prueba = 16**3
    data = np.zeros(cantidad_puntos_prueba)
    data[::tiempo_entre_puntos] = magnitud_prueba

    # Calcular la DFT
    tiempo_inicio = time.time()
    resultado = manual_dft(data)
    tiempo_fin = time.time()
    duracion_funcion = tiempo_fin - tiempo_inicio

    # Print el resultado
    print("Tiempo de la transformada en segundos: " + str(duracion_funcion))
    #print("Resultado de la transformada:")
    #print(resultado)
