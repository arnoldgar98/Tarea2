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
emec=datos[:,6]

datos1= np.genfromtxt("datos1.dat",delimiter=";")
x1=datos1[:,0]
y1=datos1[:,1]
vx1=datos1[:,2]
vy1=datos1[:,3]
mome1=datos1[:,4]
tiem1=datos1[:,5]
emec1=datos1[:,6]

datos2= np.genfromtxt("datos2.dat",delimiter=";")
x2=datos2[:,0]
y2=datos2[:,1]
vx2=datos2[:,2]
vy2=datos2[:,3]
mome2=datos2[:,4]
tiem2=datos2[:,5]
emec2=datos2[:,6]

#leap
datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=datos3[:,0]
y3=datos3[:,1]
vx3=datos3[:,2]
vy3=datos3[:,3]
mome3=datos3[:,4]
tiem3=datos3[:,5]
emec3=datos3[:,6]

datos4= np.genfromtxt("datos4.dat",delimiter=";")
x4=datos4[:,0]
y4=datos4[:,1]
vx4=datos4[:,2]
vy4=datos4[:,3]
mome4=datos4[:,4]
tiem4=datos4[:,5]
emec4=datos4[:,6]

datos5= np.genfromtxt("datos5.dat",delimiter=";")
x5=datos5[:,0]
y5=datos5[:,1]
vx5=datos5[:,2]
vy5=datos5[:,3]
mome5=datos5[:,4]
tiem5=datos5[:,5]
emec5=datos5[:,6]
#rungekutta
datos6= np.genfromtxt("datos6.dat",delimiter=";")
x6=datos6[:,0]
y6=datos6[:,1]
vx6=datos6[:,2]
vy6=datos6[:,3]
mome6=datos6[:,4]
tiem6=datos6[:,5]
emec6=datos6[:,6]

datos7= np.genfromtxt("datos7.dat",delimiter=";")
x7=datos7[:,0]
y7=datos7[:,1]
vx7=datos7[:,2]
vy7=datos7[:,3]
mome7=datos7[:,4]
tiem7=datos7[:,5]
emec7=datos7[:,6]

datos8= np.genfromtxt("datos8.dat",delimiter=";")
x8=datos8[:,0]
y8=datos8[:,1]
vx8=datos8[:,2]
vy8=datos8[:,3]
mome8=datos8[:,4]
tiem8=datos8[:,5]
emec8=datos8[:,6]
#Graficas de todos los metodos(sin momento ni energia)
plt.figure()
plt.subplot(3,3,1)
plt.plot(x,y)
plt.title("Euler dt=0.01")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,2)
plt.plot(x1,y1)
plt.title("Euler dt=0.001")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,3)
plt.plot(x2,y2)
plt.title("Euler dt=0.0001")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,4)
plt.plot(x3,y3)
plt.title("Leapfrog dt=0.01")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,5)
plt.plot(x4,y4)
plt.title("Leapfrog dt=0.001")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,6)
plt.plot(x5,y5)
plt.title("Leapfrog dt=0.006")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,7)
plt.plot(x6,y6)
plt.title("Rungekutta dt=0.01")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,8)
plt.plot(x7,y7)
plt.title("Rungekutta dt=0.001")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(3,3,9)
plt.plot(x8,y8)
plt.title("Rungekutta dt=0.0001")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("primero.png")


##Para las velocidades de todos los metodos
plt.figure()
plt.subplot(3,3,1)
plt.plot(vx,vy)
plt.title("Euler dt=0.01")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,2)
plt.plot(vx1,vy1)
plt.title("Euler dt=0.001")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,3)
plt.plot(vx2,vy2)
plt.title("Euler dt=0.0001")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,4)
plt.plot(vx3,vy3)
plt.title("Leapfrog dt=0.01")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,5)
plt.plot(vx4,vy4)
plt.title("Leapfrog dt=0.001")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,6)
plt.plot(vx5,vy5)
plt.title("Leapfrog dt=0.006")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,7)
plt.plot(vx6,vy6)
plt.title("Rungekutta dt=0.01")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,8)
plt.plot(vx7,vy7)
plt.title("Rungekutta dt=0.001")
plt.xlabel("VX")
plt.ylabel("VY")

plt.subplot(3,3,9)
plt.plot(vx8,vy8)
plt.title("Rungekutta dt=0.0001")
plt.xlabel("VX")
plt.ylabel("VY")
plt.savefig("segundo.png")

#Momento de todos los metodos
plt.figure()
plt.subplot(3,3,1)
plt.plot(tiem,mome)
plt.title("Euler dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,2)
plt.plot(tiem1,mome1)
plt.title("Euler dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,3)
plt.plot(tiem2,mome2)
plt.title("Euler dt=0.0001")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,4)
plt.plot(tiem3,mome3)
plt.title("Leapfrog dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,5)
plt.plot(tiem4,mome4)
plt.title("Leapfrog dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,6)
plt.plot(tiem5,mome5)
plt.title("Leapfrog dt=0.006")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,7)
plt.plot(tiem6,mome6)
plt.title("Rungekutta dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,8)
plt.plot(tiem7,mome7)
plt.title("Rungekutta dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("momento")

plt.subplot(3,3,9)
plt.plot(tiem8,mome8)
plt.title("Rungekutta dt=0.0001")
plt.xlabel("tiempo")
plt.ylabel("momento")
plt.savefig("tercera.png")

#Energia mecanica de las orbitas
plt.figure()
plt.subplot(3,3,1)
plt.plot(tiem,emec)
plt.title("Euler dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,2)
plt.plot(tiem1,emec1)
plt.title("Euler dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,3)
plt.plot(tiem2,emec2)
plt.title("Euler dt=0.0001")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,4)
plt.plot(tiem3,emec3)
plt.title("Leapfrog dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,5)
plt.plot(tiem4,emec4)
plt.title("Leapfrog dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,6)
plt.plot(tiem5,emec5)
plt.title("Leapfrog dt=0.006")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,7)
plt.plot(tiem6,emec6)
plt.title("Rungekutta dt=0.01")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,8)
plt.plot(tiem7,emec7)
plt.title("Rungekutta dt=0.001")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")

plt.subplot(3,3,9)
plt.plot(tiem8,emec8)
plt.title("Rungekutta dt=0.0001")
plt.xlabel("tiempo")
plt.ylabel("Emecanica")
plt.savefig("cuarta.png")