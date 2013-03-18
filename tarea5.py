# ******************************************************************
# ******************** Universidad de los Andes ********************
# ********************   Fisica computacional   ********************
# ********************         Tarea 5          ********************
# ******************************************************************
# ***************   Andres Felipe Garcia Albarracin  ***************
# ***************         Andrea Rozo Mendez	     ***************
# ****************************************************************** 

# Librerias
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy
from scipy.fftpack import fft, fftfreq

# Lectura del archivo
c = np.loadtxt('monthrg.txt')

# Vector de meses
(fil, col) = np.shape(c)
meses = []
for i in range(fil):
	meses = np.append(meses,[i])

anos = meses/12.0 + c[0,0] 
# Vector del numero de manchas
manchas = (c[:,3])

# Grafica numero de manchas en funcion del tiempo
pylab.scatter(anos,manchas)
pylab.xlabel('Ano')
pylab.ylabel('N(n)')
pylab.title('Numero de manchas solares en funcion del anho')
pylab.grid(True)
pylab.savefig('GraficaManchas')


# Transformada de Fourier
n = fil
dt = 1 							# 1 mes de intervalo
fft_manchas = np.fft.fft(manchas)/n 			# Transformada de Fourier normalizada
freq = np.fft.fftfreq(n,dt)				# Vector de frecuencias

fig1 = plt.figure()
pylab.plot(freq,abs(fft_manchas))
pylab.xlabel('$f\ [1/mes]$')
pylab.ylabel('$F\{N\}(f)\ [manchas.mes]$')
pylab.title('$\mathrm{Espectro\ de\ frecuencias\ del\ numero\ de\ manchas}$', fontsize=20)
pylab.grid(True)
pylab.savefig('TransfManchas')



