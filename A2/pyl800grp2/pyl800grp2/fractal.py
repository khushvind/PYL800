import numpy as np
import matplotlib.pyplot as plt

gsize = 1000
xvl =  np.linspace(-1.25,1.25,gsize)
def f(x):
    return x**3 -1
def f1(x):
    return 3*x**2 
delta  = 1e-7

points  = np.zeros((gsize,gsize))
#roots already known
r1 = -0.5-0.8660254j
r2 = -0.5 +0.8660254j
r3=1

for r in range(gsize):
    for i in range(gsize):
        e = xvl[r] + xvl[i]*1j
        for n in range(40):
            en  = e - f(e)/f1(e)
            if abs(en-e)<delta:
                if abs(en-r1)<delta:
                    points[i][r]=1
                    break
                if abs(en-r2)<delta:
                    points[i][r]=2
                    break
                points[i][r]=3
                break
            e=en
fractal = plt.figure()
axes = fractal.add_subplot(111)
y = axes.matshow(points,interpolation  = 'nearest',origin = 'lower')
fractal.colorbar(y)

plt.show()

