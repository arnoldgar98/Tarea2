import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

#euler
datos= np.genfromtxt("datos.dat",delimiter=";")
x=datos[:,0]
y=datos[:,1]
vx=datos[:,2]
vy=datos[:,3]
mome=datos[:,4]
tiem=datos[:,5]

datos1= np.genfromtxt("datos1.dat",delimiter=";")
x1=datos1[:,0]
y1=datos1[:,1]
vx1=datos1[:,2]
vy1=datos1[:,3]
mome1=datos1[:,4]
tiem1=datos1[:,5]

datos2= np.genfromtxt("datos2.dat",delimiter=";")
x2=datos2[:,0]
y2=datos2[:,1]
vx2=datos2[:,2]
vy2=datos2[:,3]
mome2=datos2[:,4]
tiem2=datos2[:,5]

#leap
datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=datos3[:,0]
y3=datos3[:,1]
vx3=datos3[:,2]
vy3=datos3[:,3]
mome3=datos3[:,4]
tiem3=datos3[:,5]

datos4= np.genfromtxt("datos4.dat",delimiter=";")
x4=datos4[:,0]
y4=datos4[:,1]
vx4=datos4[:,2]
vy4=datos4[:,3]
mome4=datos4[:,4]
tiem4=datos4[:,5]

datos5= np.genfromtxt("datos5.dat",delimiter=";")
x5=datos5[:,0]
y5=datos5[:,1]
vx5=datos5[:,2]
vy5=datos5[:,3]
mome5=datos5[:,4]
tiem5=datos5[:,5]
#rungekutta
datos6= np.genfromtxt("datos6.dat",delimiter=";")
x6=datos6[:,0]
y6=datos6[:,1]
vx6=datos6[:,2]
vy6=datos6[:,3]
mome6=datos6[:,4]
tiem6=datos6[:,5]

datos7= np.genfromtxt("datos7.dat",delimiter=";")
x7=datos7[:,0]
y7=datos7[:,1]
vx7=datos7[:,2]
vy7=datos7[:,3]
mome7=datos7[:,4]
tiem7=datos7[:,5]

datos8= np.genfromtxt("datos8.dat",delimiter=";")
x8=datos8[:,0]
y8=datos8[:,1]
vx8=datos8[:,2]
vy8=datos8[:,3]
mome8=datos8[:,4]
tiem8=datos8[:,5]
#Graficas de todos los metodos(sin momento ni energia)
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


##Para las velocidades de todos los metodos
plt.figure()
plt.subplot(3,3,1)
plt.plot(vx,vy)

plt.subplot(3,3,2)
plt.plot(vx1,vy1)

plt.subplot(3,3,3)
plt.plot(vx2,vy2)

plt.subplot(3,3,4)
plt.plot(vx3,vy3)

plt.subplot(3,3,5)
plt.plot(vx4,vy4)

plt.subplot(3,3,6)
plt.plot(vx5,vy5)

plt.subplot(3,3,7)
plt.plot(vx6,vy6)

plt.subplot(3,3,8)
plt.plot(vx7,vy7)

plt.subplot(3,3,9)
plt.plot(vx8,vy8)
plt.savefig("segundo.png")

#Momento de todos los metodos
plt.figure()
plt.subplot(3,3,1)
plt.plot(tiem,mome)

plt.subplot(3,3,2)
plt.plot(tiem1,mome1)

plt.subplot(3,3,3)
plt.plot(tiem2,mome2)

plt.subplot(3,3,4)
plt.plot(tiem3,mome3)

plt.subplot(3,3,5)
plt.plot(tiem4,mome4)

plt.subplot(3,3,6)
plt.plot(tiem5,mome5)

plt.subplot(3,3,7)
plt.plot(tiem6,mome6)

plt.subplot(3,3,8)
plt.plot(tiem7,mome7)

plt.subplot(3,3,9)
plt.plot(tiem8,mome8)
plt.savefig("tercera.png")