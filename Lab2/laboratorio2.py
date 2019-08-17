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
import time
import matplotlib.pylab as plt
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

#3ro en veremos

###ODES 

    