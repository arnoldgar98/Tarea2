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

##filtro de las frecuencias
def gausiana():
    


#Inversa para poder graficar
invtrans= ifft2(trans2d)     
invtrans2= ifft2(trans2d2)
plt.figure()
plt.imshow(abs(invtrans),norm=LogNorm())
plt.imshow(abs(invtrans2),norm=LogNorm())
plt.xlabel("frecuencias")
plt.ylabel("Inversa")
plt.title("Imagen mejorada")
plt.savefig("ImFiltrada.png")
