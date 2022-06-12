import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
np.set_printoptions(precision=3, suppress=False)

fsC     = 300 #frec de sampleo que imita el 'continuo' cuando mas mejor
fsD     = 30  #frec de sampleo discreta. Como el ejemplo es para una senial de 1hz, segun shanon no se podria recuperar si fsD es menor o igual a 2
N       = 100
signalF = 10

t   = np.arange(0,N/fsC,1/fsC)
td  = np.arange(0,N/fsC+1/fsC,1/fsD) #un poquito mas largo para evitar erl redondeo
nd  = 0
s1  = np.zeros(len(td))
s2  = np.zeros(len(t))
s3  = np.zeros(len(t))

fig    = plt.figure()
fftAxe = fig.add_subplot ( 2,1,2      )
fftLn, = plt.plot        ( [],[],'b-',linewidth=4 )
fftAxe.grid              ( True       )
fftAxe.set_ylim          ( 0 ,0.25 )

sigAxe = fig.add_subplot(2,1,1)
sigAxe.grid(True)
sigAxe.set_xlim(-1/fsC, np.max(t)+1/fsC)
#sigAxe.set_ylim(-1,1)
sigAxe.set_ylim(0,10)

ln1, =sigAxe.plot([],[],'ro',linewidth=8,alpha=0.8)
ln2, =sigAxe.plot([],[],'b-')
ln3, =sigAxe.plot([],[],'g-',linewidth=10,alpha=0.5)


def signal(n):
    return [5,2,8][int(n*fsD)%3] 
    #return np.sin(2*np.pi*n*signalF)

def interpolate(timeC, x, B):
    y=[]
    for t in timeC:
        prom=0
        for n in range(len(x)):
           prom += x[n]*np.sinc(2*B*t-n)
        y.append(prom)
    #input("wait press")
    #print("n:",len(x),"t:",2*B*timeC,"y:",y)
    return y

def init():
    global nd
    nd=0
    return ln1, ln2, ln3, fftLn

def update(n):
    global nd
    s2[n]=signal(t[n]) #que pasa si agrego ruido
    ln2.set_data(t[:n+1],s2[:n+1])

    if(t[n]>=td[nd]): # instantes de sampleo
        s1[nd] = signal ( td[nd] )
        sp     = s1[nd] * np.sinc ( 2*(fsD/2 )*t)
        sm     = s1[nd] * np.sinc ( 2*(fsD/2 )*-t)
        plt.plot(t+td[nd],sp,'y-',linewidth=5,alpha=0.2)
        plt.plot(td[nd]-t,sm,'y-',linewidth=5,alpha=0.2)
        ln1.set_data(td[:nd+1],s1[:nd+1])
        nd+=1
##
    s3=interpolate(t[:n+1],s1[:nd+1],fsD/2)
    ln3.set_data(t[0:len(s3)],s3)
##
    fft=np.abs ( 1/N*np.fft.fft(s2 ))**2
    fftAxe.set_ylim ( 0 ,np.max(fft)+0.01)
    fftAxe.set_xlim ( 0 ,fsC/2 )
    fftLn.set_data ( (fsC/N )*fsC*t ,fft)
    return ln1, ln2, ln3, fftLn


ani=FuncAnimation(fig,update,N,init_func=init,blit=False,interval=50,repeat=False)
#mng=plt.get_current_fig_manager()
#mng.resize(mng.window.maxsize())
plt.get_current_fig_manager().window.showMaximized() #para QT5
plt.show()

