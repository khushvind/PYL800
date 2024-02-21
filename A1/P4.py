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

P=np.array([np.array([0,0]),np.array([4,1]),np.array([-1,1]),np.array([3,0])])

t=np.linspace(0,1,num=100)

def plot(x,wt,n):        #n=order of curve
    wt=wts(wt,n)
    new_x=np.zeros(len(x))
    new_y=np.zeros(len(x))
    for i in range(n+1):
        new_x=new_x+P[i][0]*wt[i][0](x)
        new_y=new_y+P[i][1]*wt[i][0](x)
    plt.plot(new_x,new_y)
    plt.scatter(np.transpose(P)[0],np.transpose(P)[1])
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot(t,wt,3)
