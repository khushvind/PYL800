#import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 - 3*x - 6
def g(x):
    return 3 + 6/x

ini = -1 
# roots are -1.372281 and 4.372281

e = ini
delta = 1e-6
points = []
for n in range(100):
    
    en = g(e)
    points.append(en)
    if abs(en-e)<delta:
        print (n)
        
        break
    e=en
plt.plot(points)
plt.show()
print(points)


