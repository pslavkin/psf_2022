from sys import getsizeof
import numpy as np
import matplotlib.pyplot as plt

s1 = np.array([20,10,30]) #array de 3
s  = np.tile(s1,3)        #replica un array n veces
s=[np.sin(2*np.pi*3*t*1/30) for t in range(20)]

#linspace asegura la cantidad de valores
t = np.linspace (0 ,len(s) ,len(s))
print(len(t) ,t ,getsizeof(t))

plt.plot(t,s,'ro-')
plt.show()

exit()

#numpy arrays
s=[np.sin(2*np.pi*3*t*1/20) for t in range(100)]

#generators
t=(i**2 for i in range(9))
print(next(t),next(t),next(t))

#generators con funciones
def signal(frec,fs):
    t=0
    while True:
        yield np.sin(2*np.pi*frec*t*1/fs)
        t+=1

a=signal(3,20)
s=np.array([next(a) for i in range(9)])

#generators in line
a=(np.sin(2*np.pi*3*t*1/20) for t in range(100))
s=np.array([next(a) for i in range(100)])

#base de tiempo
#--------------------
#arange asegura el paso
t=np.arange(0,len(s),1) #base de tiempo de 0 a 3 (no inclusive) en pasos de 1
print(len(t),t,getsizeof(t))

