import numpy as np
import matplotlib.pylab as plt
datos= np.genfromtxt("datos.dat",delimiter=";")
x=datos[:,0]
y=datos[:,1]
plt.figure()
plt.plot(x,y)
plt.savefig("primero.png")
