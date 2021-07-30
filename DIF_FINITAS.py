# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 23:55:55 2021

@author: Denisse Molina
"""
## DIFERENCIAS FINITAS
## GRUPO 8
## 30/07/2021

# LIBRERIA 

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# DATOS

cc1=(60,61,62,63,64,65,66,67,68,69,70,71)
cc2=(50,52,54,56,58,60,62,64,66,68,70,72)
ci=[50,51,52,53,54,55,56,57,58,59,60,61]
n=10     #Número de nodos
x1=np.linspace(0,1,11)
y1=np.linspace(0,1,11)


# CODIGO ELABORADO 
#h es delta x
#t es delta t
h=0.1
t=0.001
alpha=1     
k=alpha*t/(h**2)

T=np.zeros((n+1,n+1))
for i in range(n+1):
    T[0][i]=ci[i]
    T[i][0]=cc2[i]
    T[i][n]=cc1[i]
    T[0][i]=ci[i]
    T[0][10]=60
    
print("\n\n  MATRIZ")
print ("\n",T)

for i in range (1,n+1):
    for j in range(0,n-1): 
        T[i][j+1]=(k*(T[i-1][j]-(2*T[i-1][j+1])+T[i-1][j+2]))+T[i-1][j+1]

print("\n\n  DIFERENCIAS FINITAS")
print("\n",T)

# GRAFICO 

plt.plot(T)
fig=plt.figure()
ax=Axes3D(fig)
#g=ax.contour(x1,y1,T)
surface=ax.plot_surface(x1,y1,T)
plt.show()
    