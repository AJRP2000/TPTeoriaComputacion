import numpy as np
import time

def cooley_tukey_fft(tren_de_impulso):
    # Get the length of the input array
    N = len(tren_de_impulso)

    # Check if N is not a power of 2
    if not (N & (N - 1) == 0) and N > 0:
        # Calculate the next power of 2 greater than or equal to N
        padded_N = 2 ** (N - 1).bit_length()
        
        # Zero-pad the input array to the next power of 2
        tren_de_impulso = np.pad(tren_de_impulso, (0, padded_N - N), 'constant')

    # Perform the Cooley-Tukey FFT as before
    if N <= 1:
        return tren_de_impulso
    else:
        par = cooley_tukey_fft(tren_de_impulso[0::2])
        impar = cooley_tukey_fft(tren_de_impulso[1::2])
        T = [np.exp(-2j * np.pi * k / N) * impar[k] for k in range(N // 2)]
        return [par[k] + T[k] for k in range(N // 2)] + [par[k] - T[k] for k in range(N // 2)]


def test():
    tiempo_entre_puntos = 1
    magnitud_prueba = 1
    cantidad_puntos_prueba = 3**1
    data = np.zeros(cantidad_puntos_prueba)
    data[::tiempo_entre_puntos] = magnitud_prueba

    # Calculate the DFT
    tiempo_inicio = time.time()
    resultado = cooley_tukey_fft(data)
    tiempo_fin = time.time()
    duracion_funcion = tiempo_fin - tiempo_inicio

    # Print the resultado
    print("Tiempo de la transformada en segundos: " + str(duracion_funcion))
    #print("Resultado de la transformada:")
    #print(resultado)
    