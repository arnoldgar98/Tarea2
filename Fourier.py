#paquetes
import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2
from matplotlib.colors import LogNorm

#almaceno las dos imagenes
imagen1= plt.imread("cara_02_grisesMF.png")
imagen2= plt.imread("cara_03_grisesMF.png")

#saco la transformada rapida de fourier de las imagenes y la grafico
trans2d = fft2(imagen1)
trans2d2= fft2(imagen2)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(abs(trans2d),norm=LogNorm())
plt.colorbar()
plt.title("transformada imagen seria")

plt.subplot(1,2,2)
plt.imshow(abs(trans2d2),norm=LogNorm())
plt.title("transformada imagen sonriendo")
plt.colorbar()
plt.savefig("FFtIm.pdf")

#De acuerdo al paper enviado por sicua, para obtener una imagen hibrida es necesario hacer un filtro para las frecuencias bajas y otro para las frecuencias altas
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
            if(abs(frec[i,j])<110):
                frec[i,j]=0
    return frec
def filtrobajas(frec):
    for i in range(np.shape(frec)[0]):
        for j in range(np.shape(frec)[1]):
            if(abs(frec[i,j])>45):
                frec[i,j]=0
    return frec

frecfiltro1 = filtroaltas(frecimagen2) 
frecfiltro2 = filtrobajas(frecimagen)
##Para calibrar mejor la imagen es posible multiplicar la inversa por valores entre 0 y 1.( consejo de veronica)
inversa1=np.fft.ifftshift(frecfiltro1)
inversa2=np.fft.ifftshift(frecfiltro2)
total=ifft2(inversa1)*0.48+ ifft2(inversa2)*0.8
    
    

#Inversa para poder graficar
     

plt.figure()
plt.imshow(abs(total),cmap='gray')
plt.xlabel("frecuencias")
plt.ylabel("Inversa")
plt.title("Imagen mejorada")
plt.savefig("ImFiltrada.png")
