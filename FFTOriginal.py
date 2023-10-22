import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
import time

def unit_step_impulse_train_fourier(sampling_rate, num_samples):
    
    # Create the unit step impulse train signal
    impulse_train = np.zeros(num_samples)
    impulse_train[::sampling_rate] = 1  # Impulses at multiples of the sampling rate
    
    
    start_time = time.time()
    # Compute the Fourier Transform
    fft_result = fft(impulse_train)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
    
    return fft_result

# Example usage
sampling_rate = 1  # Hz
num_samples = 10**7


fft_result = unit_step_impulse_train_fourier(sampling_rate, num_samples)

# Calculate the corresponding frequencies
frequencies = np.fft.fftfreq(num_samples, 1/num_samples)

# Plot the magnitude of the Fourier Transform
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(fft_result))
plt.title("Transformada de Fourier del tren de impulso del escalon unitario")
plt.xlabel("Frecuencia en N")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()

a = 2