import time
import matplotlib.pylab as plt
import numpy as np

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
plt.title("Fibonacci recursivo")
plt.savefig("primera.png")

#3er punto
#sin usar la recursividad y como lo plantea el problema, el objetivo es optimizar el metodo de fibonnacci
def fib(n):
    b=0
    a=1
    for i in range(1,n):
        b=a+b
        a=b
    return a
tiempos2=[]
diferencias2=[]
for i in range(1,101):
    init= time.time()
    fib(i)
    difference_time=time.time()-init
    tiempos2.append(i)
    diferencias2.append(difference_time)
plt.figure()
plt.plot(tiempos2,diferencias2)
plt.xlabel("Tiempos")
plt.ylabel("Diferencias de tiempo")
plt.title("Fibonacci")
plt.savefig("Optimizada")
#4 Para comprobar la convergencia del metodo de fibonacci se procede a hacer lo que dice en el enunciado: Fn+1/Fn  for every n and plot this ratio in function of n. Where does it converge (if it does)?
listadef=[]
listan=[]
for i in range(1,101):
    f=fib(i+1)/fib(i)
    listadef.append(f)
    listan.append(i)    
plt.figure()
plt.scatter(listadef, listan)
plt.savefig("convergencia")
print("para cada n iteración de la serie de fibonacci el metodo converge a 2, a excepción del primer termino que hace referencia al valor de 1 ")    
    
### SEGUNDO PUNTO METODO DE EULER
#defino la derivada
def dyent(t0,y0):
    return 2-np.exp(-4*t0)-2*y0

puntos=100
a=0
b=1
#Espaciado
h=(b-a)/puntos
t=np.ones(puntos)
y=np.ones(puntos)
#condiciones iniciales dadas por el enunciado
t[0]=0
y[0]=1
for i in range(1,puntos):
    #avance del tiempo
    t[i]= t[i-1]+h
    y[i]= y[i-1]+(h*dyent(t[i-1],y[i-1]))
    
#la analitica dada por el enunciado para comparar el metodo del euler con la solucion teorica, y así calcular el error
def analitica(x0):
    return 1+0.5*np.exp(-4*x0)-0.5*np.exp(-2*x0)

plt.figure()
plt.plot(t,y)
plt.plot(t,analitica(t))
plt.xlabel("Tiempo")
plt.ylabel("Euler y analitica")
plt.title("Euler y Analitica")
plt.savefig("total")    

#Errores
error=np.abs(analitica(t)-y)/analitica(t)
plt.figure()
plt.plot(t,error)
plt.xlabel("Tiempo")
plt.ylabel("Error")
plt.title("Tiempo vs Error")
plt.savefig("Loserrores.png")

#promedio de los errores
pendientes=error
promedio=np.sum(pendientes)/(puntos+1)
print("promedio de errores despues de hacer valor analitica-experimental/analitico es de ",promedio)
        
           

### TERCER PUNTO 
#se hace el orden ascendente de la lista
lista=[1,3,2,8,6]
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j]>lista[i]:
            temp=lista[i]
            lista[i]=lista[j]
            lista[j]=temp
#se crea una nueva lista con listas dentro del tamaño del numero correspondiente            
listan=[]
for i in range(len(lista)):
    listatemp=lista[i]
    temp=[listatemp]*listatemp
    listan.append(temp)
print(listan) 

    