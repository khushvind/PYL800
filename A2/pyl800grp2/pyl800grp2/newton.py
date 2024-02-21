#import numpy as np
import matplotlib.pyplot as plt 
def f(x):
    #use other functions for complex roots
    #return x**5+ x**4 +5*x**2 +6
    return x**2 - 3*x - 6
def f1(x):
    #return 5*x**4 + 4*x**3+10*x
    return 2*x - 3
delta  = 1e-13
points = []
x =[]
y=[]
ini = -1
e = ini
for n in range(50):
    en = e-f(e)/f1(e)
    points.append(en)
    x.append(en.real)
    y.append(en.imag)
    if abs(en-e)<delta:
        print("iterations : ")
        print(n)
        break
    e=en
print(points)
plt.plot(x,y,'o')
plt.show()