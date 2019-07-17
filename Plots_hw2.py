import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

#euler
datos= np.genfromtxt("datos.dat",delimiter=";")
x=datos[:,0]
y=datos[:,1]

datos1= np.genfromtxt("datos1.dat",delimiter=";")
x1=datos1[:,0]
y1=datos1[:,1]

datos2= np.genfromtxt("datos2.dat",delimiter=";")
x2=datos2[:,0]
y2=datos2[:,1]
#leap
datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=datos3[:,0]
y3=datos3[:,1]

datos4= np.genfromtxt("datos4.dat",delimiter=";")
x4=datos4[:,0]
y4=datos4[:,1]

datos5= np.genfromtxt("datos5.dat",delimiter=";")
x5=datos5[:,0]
y5=datos5[:,1]
#rungekutta
datos6= np.genfromtxt("datos6.dat",delimiter=";")
x6=datos6[:,0]
y6=datos6[:,1]

datos7= np.genfromtxt("datos7.dat",delimiter=";")
x7=datos7[:,0]
y7=datos7[:,1]

datos8= np.genfromtxt("datos8.dat",delimiter=";")
x8=datos8[:,0]
y8=datos8[:,1]

plt.figure()
plt.subplot(3,3,1)
plt.plot(x,y)

plt.subplot(3,3,2)
plt.plot(x1,y1)

plt.subplot(3,3,3)
plt.plot(x2,y2)

plt.subplot(3,3,4)
plt.plot(x3,y3)

plt.subplot(3,3,5)
plt.plot(x4,y4)

plt.subplot(3,3,6)
plt.plot(x5,y5)

plt.subplot(3,3,7)
plt.plot(x6,y6)

plt.subplot(3,3,8)
plt.plot(x7,y7)

plt.subplot(3,3,9)
plt.plot(x8,y8)
plt.savefig("primero.png")

