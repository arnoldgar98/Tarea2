import time
import matplotlib.pylab as plt
import numpy as np
'''
#1er punto
def fib_recursion(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    else: 
        return fib_recursion(n-1)+fib_recursion(n-2)
print(fib_recursion(20))

# 2do punto

tiempos=[]
diferencias=[]
for i in range(1,41):
    init=time.time()
    fib_recursion(i)
    difference_time=time.time()-init
    tiempos.append(i)
    diferencias.append(difference_time)
    
plt.figure()
plt.plot(tiempos,diferencias)
plt.xlabel("Tiempos")
plt.ylabel("Diferencias")
plt.title("Tiempo")
plt.savefig("primera.png")
'''

### SEGUNDO PUNTO METODO DE EULER
#defino la derivada
def funcion(y1,t1):
    return 2 - np.exp(-4*t1)-2*y1

#Acá declaro las condiciones iniciales y los arreglos necesarios para poder resolver la ecuacion diferencial
ini = 0
final = 1
puntos = 100
dy = (final-ini)/puntos
y= np.zeros(puntos)
t= np.zeros(puntos)


y[0]=1
t[0]=0

#FInalmente se crea el bucle que va a llenar los arreglos con la solución a la ecuacin diferencial, para esto se debe tomar el metodo de Euler el cual me actualiza la solución de un punto tomando el valor de la derivada en el punto anterior multiplicado por un delta.
for i in range(1,puntos):
    t[i]=t[i-1]+dy
    y[i]=y[i-1]+(dy*funcion(y[i-1],t[i-1]))

plt.figure()
plt.plot(t,y, color = "green", marker = "o")
plt.xlabel("$t$")
plt.ylabel("$y(t)$")
plt.savefig("SolucionODE")

  
        
           
'''
### TERCER PUNTO 
#se hace el orden ascendente de la lista
lista=[1,3,2,8,6]
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j]>lista[i]:
            temporal=lista[i]
            lista[i]=lista[j]
            lista[j]=temporal
#se crea una nueva lista con listas dentro del tamaño del numero correspondiente            
listan=[]
for i in range(len(lista)):
    listatemp=lista[i]
    temp=[listatemp]*listatemp
    listan.append(temp)
print(listan)
   '''  

    