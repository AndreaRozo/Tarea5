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
c = np.loadtxt('monthrg2.txt')

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
pylab.xlabel('$A\~no$')
pylab.ylabel('$N(n)$')
pylab.title('$\mathrm{Numero\ de\ manchas\ solares\ en\ funcion\ del\ a\~no}$', fontsize=20)
pylab.grid(True)
pylab.savefig('GraficaManchas')


# Transformada de Fourier
n = fil
dt = 1 							# 1 mes de intervalo
fft_manchas = np.fft.fft(manchas)/n 			# Transformada de Fourier normalizada
freq = np.fft.fftfreq(n,dt)				# Vector de frecuencias
fft_manchas_shift = np.fft.fftshift(fft_manchas)
freq_shifted = np.fft.fftshift(freq)


# Espectro de potencias
f2 = abs(fft_manchas_shift)*abs(fft_manchas_shift)

fig1 = plt.figure()
pylab.plot(freq_shifted,abs(f2))
pylab.xlabel('$f\ [1/mes]$')
pylab.ylabel('$(F\{N\})^2(f)\ [manchas.mes]^2$')
pylab.title('$\mathrm{Espectro\ de\ potencias\ del\ numero\ de\ manchas}$', fontsize=20)
pylab.grid(True)
pylab.savefig('PotenciaManchas')

# Espectro de frecuencias en funcion del periodo T
m = np.size(freq_shifted)
per = 1/(12*freq_shifted[m/(20*12)+m/2:m/12+m/2])
f3 = f2[m/(20*12)+m/2:m/12+m/2]
fig2 = plt.figure()
pylab.plot(per,abs(f3))
pylab.xlabel('$T\ [a\~no]$')
pylab.ylabel('$(F\{N\})^2(T)\ [manchas.mes]^2$')
pylab.title('$\mathrm{Espectro\ de\ potencias\ del\ numero\ de\ manchas}$', fontsize=20)
pylab.grid(True)
pylab.savefig('PotenciaManchasPeriodo')

# Filtro pasa-bajas
fft_filtrado = fft_manchas_shift
freq_corte = 1/12.0
for i in range(len(freq_shifted)):
        if(abs(freq_shifted[i]) > freq_corte):
           fft_filtrado[i] = 0.0

f4 = abs(fft_filtrado)*abs(fft_filtrado)
inv_filtro = np.fft.ifft(fft_filtrado)*n

fig3 = plt.figure()
pylab.plot(freq_shifted,abs(f4))
pylab.xlabel('$f\ [1/mes]$')
pylab.ylabel('$(F\{N\})^2(f)\ [manchas.mes]^2$')
pylab.title('$\mathrm{Espectro\ de\ potencias\ del\ numero\ de\ manchas\ con\ filtro}$', fontsize=18)
pylab.grid(True)
pylab.savefig('PotenciaManchasFiltradas')

fig4 = plt.figure()
pylab.scatter(anos,abs(np.real(inv_filtro)))
pylab.xlabel('$A\~no$')
pylab.ylabel('$N(n)$')
pylab.title('$\mathrm{Numero\ de\ manchas\ solares\ limpias\ en\ funcion\ del\ a\~no}$', fontsize=18)
pylab.grid(True)
pylab.savefig('GraficaManchasLimpias')

# Grafica comparativa
fig4 = plt.figure()
pylab.plot(anos,manchas,'bo',anos,abs(np.real(inv_filtro)),'ro')
pylab.xlabel('$A\~no$')
pylab.ylabel('$N(n)$')
pylab.title('$\mathrm{Numero\ de\ manchas\ solares\ en\ funcion\ del\ a\~no}$', fontsize=18)
pylab.grid(True)
pylab.savefig('GraficaComparativaManchas')

# Proximo maximo
p = np.where(f3 == f3.max())
perMax = float(per[p[0]])
print "Periodo para que se presente un maximo: ",perMax

f5 = abs(np.real(inv_filtro))
mA = np.where(f5 == f5.max())
mxA = float(anos[mA[0]])

f6 = f5[int(mA[0])+1:len(f5)]
miA = np.where(f6 == f6.min())
minA = float(anos[miA[0]+mA[0]+1])

f7 = f6[int(miA[0])+1:len(f6)]
maA = np.where(f7 == f7.max())
maxA = float(anos[maA[0]+miA[0]+1+mA[0]+1])

proxMax = maxA + perMax
print "Proximo maximo: ",proxMax,'\n'
print "Proximos cinco maximos: \n",proxMax,'\n',proxMax+perMax,'\n',proxMax+perMax+perMax,'\n',proxMax+perMax+perMax+perMax,'\n',proxMax+perMax+perMax+perMax+perMax

