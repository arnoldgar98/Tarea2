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

plt.figure(figsize=(15,15))
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
plt.figure(figsize=(15,15))
plt.subplot(3,2,1)
plt.imshow(abs(frecimagen),norm= LogNorm())
plt.title("frecuencias de la seria")
plt.colorbar()
plt.subplot(3,2,2)
plt.imshow(abs(frecimagen2),norm= LogNorm())
plt.title("frecuencias sonriendo")
plt.colorbar()


##filtros, la aplicacion del filtro se hizo a prueba y error de acuerdo a la imagen que mejor se veia
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


plt.subplot(3,2,3)
plt.imshow(abs(frecfiltro2),norm= LogNorm())
plt.title("frecuencias despues de filtro(seria)")
plt.colorbar()
plt.subplot(3,2,4)
plt.imshow(abs(frecfiltro1),norm= LogNorm())
plt.title("frecuencias despues de filtro(sonriendo)")
plt.colorbar()
##Para calibrar mejor la imagen es posible multiplicar la inversa por valores entre 0 y 1.( consejo de veronica)
inversa1=np.fft.ifftshift(frecfiltro1)
inversa2=np.fft.ifftshift(frecfiltro2)
total=ifft2(inversa1)*0.4+ ifft2(inversa2)*0.8

prueba1=ifft2(inversa1)
prueba2=ifft2(inversa2)

plt.subplot(3,2,5)
plt.imshow(abs(prueba2),norm= LogNorm())
plt.title("Imagen con filtro(seria)")
plt.colorbar()
plt.subplot(3,2,6)
plt.imshow(abs(prueba1),norm= LogNorm())
plt.title("Imagen con filtro(sonriendo)")
plt.colorbar()
plt.savefig("ImProceso.pdf")
    
    

#Inversa para poder graficar
     

plt.figure()
plt.imshow(abs(total),cmap='gray')
plt.xlabel("frecuencias")
plt.ylabel("Inversa")
plt.title("Imagen mejorada")
plt.savefig("ImHybrid.pdf")
