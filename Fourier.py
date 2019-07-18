#paquetes
import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2
from matplotlib.colors import LogNorm

#almacenar las dos imagenes
imagen1= plt.imread("cara_02_grisesMF.png")
imagen2= plt.imread("cara_03_grisesMF.png")
#transformada 
trans2d = fft2(imagen1)
trans2d2= fft2(imagen2)
#muestra
##imagenes de la transformada y las frecuencias
plt.figure()
plt.subplot(1,2,1)
plt.imshow(abs(trans2d),norm=LogNorm(vmin=5))
plt.title("transformada de fourier")
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(abs(trans2d2),norm=LogNorm(vmin=5))
plt.title("transformada de fourier")
plt.colorbar()
plt.savefig("FFT2D.png")
#frecuencias
frecimagen=np.fft.fftshift(trans2d)
frecimagen2=np.fft.fftshift(trans2d2)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(abs(frecimagen),norm= LogNorm())
plt.title("transformada de fourier")
plt.colorbar()
plt.subplot(1,2,2)
plt.imshow(abs(frecimagen2),norm= LogNorm())
plt.title("transformada de fourier")
plt.colorbar()
plt.savefig("frecuencias")

##filtros
def filtroaltas(frec):
    for i in range(np.shape(frec)[0]):
        for j in range(np.shape(frec)[1]):
            if(frec[i,j]>10):
                frec[i,j]=0
    return frec
def filtrobajas(frec):
    for i in range(np.shape(frec)[0]):
        for j in range(np.shape(frec)[1]):
            if(frec[i,j]<9):
                frec[i,j]=0
    return frec

frecfiltro1 = filtroaltas(frecimagen) 
frecfiltro2 = filtrobajas(frecimagen2)
    
total= np.zeros([np.shape(trans2d)[0],np.shape(trans2d)[1]])
inversa1=np.fft.ifftshift(frecfiltro1)
inversa2=np.fft.ifftshift(frecfiltro2)
total=inversa1+inversa2
    
    

#Inversa para poder graficar
invtrans= ifft2(total)     

plt.figure()
plt.imshow(abs(invtrans),norm=LogNorm(),cmap='gray')
plt.xlabel("frecuencias")
plt.ylabel("Inversa")
plt.title("Imagen mejorada")
plt.savefig("ImFiltrada.png")
