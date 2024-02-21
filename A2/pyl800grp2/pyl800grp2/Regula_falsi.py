#!/usr/bin/env python
# coding: utf-8

# In[73]:


def f(x):
    return x**3-1


# In[74]:


def regula_falsi(a,b,e,list_of_c):
    if abs(f(a))<e:
        list_of_c.append(a)
        return a, list_of_c
    elif abs(f(b))<e:
        list_of_c.append(b)
        return b, list_of_c
    else:
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        list_of_c.append(c)
        if abs(f(c))<e:
            return c, list_of_c
        else:
            if f(a)*f(c)<0:
                return regula_falsi(a,c,e,list_of_c)
            elif f(c)*f(b)<0:
                return regula_falsi(c,b,e,list_of_c)
        


# In[75]:


root1, list_of_c1=regula_falsi(0,2,0.001,[])
print(root1)


# In[76]:


from matplotlib import pyplot as plt
x=list_of_c1
y=[]
for i in x:
    y.append(f(i))
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,'o')


# In[77]:


root2, list_of_c2=regula_falsi(0,6,0.001,[])
x=list_of_c2
print(x)
y=[]
for i in x:
    y.append(f(i))
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y,'o')


# In[67]:


import numpy as np
imaginary=np.sqrt(-1+0j)
root3, list_of_c3=regula_falsi(2*imaginary,1,0.001,[])
print(list_of_c3)
x=[ele.real for ele in list_of_c3]
y=[ele.imag for ele in list_of_c3]
plt.scatter(x,y)
plt.show()


# In[ ]:




