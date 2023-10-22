import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
import threading
import time

class ResultThread(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__(target=target, args=args)
        self._result = None

    def run(self):
        self._result = self._target(*self._args)

    def get_result(self):
        return self._result

def parallel_fft_impulse_train(num_samples, sample_rate, num_threads=2):
    # Generate an impulse train of the unit step
    impulse_train = np.zeros(num_samples)
    impulse_train[::sample_rate] = 1

    # Split the input data into even and odd values
    even_values = impulse_train[::2]
    odd_values = impulse_train[1::2]

    # Define the function to compute FFT for a given data array
    

    # Use joblib to compute FFT in parallel
    odd_thread = ResultThread(target=fft, args=(odd_values,))
    even_thread = ResultThread(target=fft, args=(even_values,))

    start_time = time.time()
    odd_thread.start()
    even_thread.start()

    odd_thread.join()
    even_thread.join()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    
    
    odd_result = odd_thread.get_result()
    even_result = even_thread.get_result()
    # Combine the results
    combined_fft = np.zeros(num_samples, dtype = "complex_")
    for x in range(num_samples):
        if(x==0 or x==1):
            combined_fft[x] =even_result[x] + odd_result[x]
        else:
            if(x % 2 == 0):
                combined_fft[x] = even_result[x//2]
            else:
                combined_fft[x] = odd_result[x//2]

    return combined_fft

# Example usage:
num_samples = 10**7  # Number of samples
sample_rate = 1    # Impulse spacing
num_threads = 2    # Number of threads

result = parallel_fft_impulse_train(num_samples, sample_rate, num_threads)
# Calculate the corresponding frequencies
frequencies = np.fft.fftfreq(num_samples, 1/num_samples)

# Plot the magnitude of the Fourier Transform
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(result))
plt.title("Transformada de Fourier del tren de impulso del escalon unitario")
plt.xlabel("Frecuencia en N")
plt.ylabel("Magnitud")
plt.grid(True)
plt.show()


a = 2