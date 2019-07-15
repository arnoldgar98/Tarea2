import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

datos= np.genfromtxt("datos.dat",delimiter=";")
x=datos[:,0]
y=datos[:,1]
t=datos[:,4]
plt.figure()
plt.plot(x,y)
plt.savefig("primero.png")


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,t,c="black",label="Tierra")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Orbitas de los planetas")
plt.legend()
plt.savefig("otro.png")