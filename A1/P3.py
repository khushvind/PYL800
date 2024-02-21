import matplotlib.pyplot as plt
import numpy as np

wt=[np.polynomial.Polynomial([1,-1]),np.polynomial.Polynomial([0,1])]

def wts(new_wt,n,ctr=1):
    global wt
    if ctr<n:
        temp=[np.polynomial.Polynomial([0])]*(len(new_wt)+1)
        for i in range(len(wt)):
            for j in range(len(new_wt)):
                temp[i+j]=np.polynomial.polynomial.polyadd(temp[i+j],(np.polynomial.polynomial.polymul(wt[i],new_wt[j])))
        return wts(temp,n,ctr+1)
    return new_wt

t=np.linspace(0,1,num=100)

def plot(x,wt,n):        #n=order of curve
    wt=wts(wt,n)
    for i in range(n+1):
        plt.plot(x,wt[i][0](x),label='P'+str(i))
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('weight')
    plt.grid()
    plt.show()

plot(t,wt,3)
