import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
    X=[]

    for k in np.arange(0,N):
        s=0
        for n in np.arange(0,N):
            s=s+x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return X
n=np.arange(0,100)
h=np.array([1,2,3,4])
N=len(n)
X=np.cos(1*np.pi*20*n/N)
x = dft(X,N)
mag = np.abs(x)
ang = np.angle(x)
plt.subplot(2,1,1)
plt.stem(mag)
plt.subplot(2,1,2)
plt.stem(ang)
plt.show()

