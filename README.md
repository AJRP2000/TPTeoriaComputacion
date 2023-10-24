# TPTeoriaComputacion

Este repositorio contiene el código y la documentación para el trabajo de fin de materia de Teoria de Computacion que explora y compara cuatro implementaciones diferentes de la Transformada de Fourier (DFT) en Python: 
1.- La DFT original (archivo: testManual.py)
2.- La DFT dividiendo los valores en pares e impares (archivo: testParImpar.py)
3.- La DFT diviendo los valores en pares e impares y aprovechando la periodicidad del exponencial de euler (archivo: testParImparComplejo.py)
4.- El algoritmo de Cooley Tukey FFT. El objetivo del trabajo es examinar la diferencia en complejidad y eficiencia entre estas dos técnicas. (archivo: testCooleyFFT.py)

La comparacion de estos algoritmos se realiza en el archivo comparacionDFT.py y se utiliza la librera time para llevar cuenta del tiempo toma cada uno de los algoritmos.

El archivo PaperTPTeoriaComputacion.docx contiene el trabajo escrito que explica los principios matematicos para la elaboracion de estos algoritmos, ademas de brindar las conclusiones de este trabajo.