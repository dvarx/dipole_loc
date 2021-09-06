import numpy as np
from math import pi
import matplotlib.pyplot as plt
from scipy.fft import fft

f0=5e3
N=1e4
Tp=1/f0
num_periods=100

times=np.linspace(0,num_periods/f0,int(N))
ms=np.zeros(10000)
for i in range(0,len(ms)):
    t=(times[i]%Tp)
    if (t>=Tp/12 and t<=5*Tp/12):
        ms[i]=1
    elif (t>=7*Tp/12 and t<=11*Tp/12):
        ms[i]=-1
    else:
        ms[i]=0

ms_dft=fft(ms)

fig,axes=plt.subplots(2,1)

axes[0].plot(np.abs(ms_dft[:int(len(ms_dft)/2)]))
axes[0].set_xlabel("Frequency f [Hz]")
axes[0].set_ylabel("Amplitude $\hat{V}$ [V]")
axes[1].plot(times,ms)
axes[1].set_xlabel("Time t [s]")
axes[1].set_ylabel("Modulation m(t)")

plt.show()