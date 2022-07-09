import numpy as np
import scipy.signal as sc
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#--------------------------------------
N=100
fig        = plt.figure(1)
fig.suptitle('Correlation - Matched filter', fontsize=16)

#senial a transmitir
h=np.ndarray(0)
h=np.append(h,0)
h=np.append(h,1)
h=np.append(h,2)
h=np.append(h,3)
h=np.append(h,4)
h=np.append(h,5)
h=np.append(h,4)
h=np.append(h,3)
h=np.append(h,2)
h=np.append(h,3)
h=np.append(h,4)
h=np.append(h,5)
h=np.append(h,4)
h=np.append(h,3)
h=np.append(h,2)
h=np.append(h,1)
h=np.append(h,0)
M=len(h)

nData = np.arange(0,N,1)
#--------------------------------------
xAxe    = fig.add_subplot(3,1,1)
xLn,    = plt.plot([],[],'r-o',linewidth             = 15,alpha       = 0.2)
xZoneLn = xAxe.fill_between([0,0],100,-100,facecolor = "yellow",alpha = 0.5)
xAxe.grid(True)
xAxe.set_ylim(-10,10)
xAxe.set_xlim(0,N-1)
xAxe.set_ylabel("señal\nrecibida",rotation=0,labelpad=20,fontsize=8,va="center")
#--------------------------------------
hAxe  = fig.add_subplot(3,1,2)
hLn,  = plt.plot([],[],'b-o',linewidth = 15,alpha = 0.2)
hAxe.grid(True)
hAxe.set_xlim(0,N-1)
hAxe.set_ylim(min(h)-0.4,max(h)+0.4)
hAxe.set_ylabel("señal\nesperada",rotation=0,labelpad=20,fontsize=8,va="center")
##--------------------------------------
yData        = np.zeros(N)
yAxe         = fig.add_subplot(3,1,3)
yLn,         = yAxe.plot([],[],'g-o',linewidth              = 15,alpha = 0.2)
yDotLn,      = yAxe.plot([],[],'ko',linewidth               = 15,alpha = 0.8)
thresholdLn, = yAxe.plot(nData,np.ones(N)*120,'r-',linewidth = 2,alpha  = 0.8)
yAxe.grid(True)
yAxe.set_xlim(0,N-1)
yAxe.set_ylim(-100,200)
yAxe.set_ylabel("correlacion",rotation=0,labelpad=20,fontsize=8,va="center")
##--------------------------------------
def init():
    global yData,x
    x=np.zeros(N)
    x[N//2:N//2+M]=h
    x[N//8:N//8+M]=h
    #x+=np.random.normal(0,2,N) #y si agrego ruido ??
    xLn.set_data(nData,x)
    yData *= 0
    return xLn,hLn,yLn,xZoneLn,yDotLn,thresholdLn,
#
def update(i):
    global hData,yData,x
    #input("actual loop: {}\r\n".format(i))
    hLn.set_data(nData[i:i+M],h)

    yData[i]=np.sum(x[i:i+M]*h) #aca esta la operacion de convolucion punto a punto
    yLn.set_data(nData,yData)
    yDotLn.set_data(i,yData[i])
    xZoneLn = xAxe.fill_between([i,i+(M-1)],100,-100,facecolor="yellow",alpha=0.5)

    return xLn,hLn,yLn,xZoneLn,yDotLn,thresholdLn,

ani=FuncAnimation(fig,update,N-M+1,init,interval=10 ,blit=True,repeat=True)
plt.get_current_fig_manager().window.showMaximized()
plt.show()
