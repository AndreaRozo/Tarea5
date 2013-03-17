# **********************************************
# ********** Universidad de los Andes **********
# **********   Fisica computacional   **********
# **********         Tarea 5          **********
# **********************************************
# Autores:
#	Andres Felipe Garcia Albarracin
#	Andrea Rozo Mendez
# ********************************************** 

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

# Vector del numero de manchas
manchas = (c[:,2])

# Grafica numero de manchas en funcion del tiempo
pylab.scatter(meses,manchas)
pylab.xlabel('Numero de mes')
pylab.ylabel('N(m)')
pylab.title('Numero de manchas solares en funcion del mes')
pylab.savefig('GraficaManchas')
pylab.grid(True)

# Transformada de Fourier
n = fil
dt = 1 					# 1 mes de intervalo
fft_manchas = fft(manchas)/n 		# Transformada de Fourier normalizada
freq = fftfreq(n,dt)			# Vector de frecuencias

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.bar(freq,abs(fft_manchas))
ax2.set_xlabel("$Frecuencia [1/mes]$",fontsize=20)
ax2.set_ylabel("$Manchas*mes$",fontsize=20)
ax2.set_title("$Transformada\ de\ Fourier\ del\ num\ de\ manchas$", fontsize=20)
filename = 'GraficaTransformada'
fig2.savefig(filename + '.jpeg',format = 'jpeg', transparent=True)



print meses
