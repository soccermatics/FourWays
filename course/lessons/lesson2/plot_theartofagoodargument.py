"""
The Art of A Good Argument
==========================

Here we...
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

n=26

#Self other 
X11=0
Y11=0.9
X01=0
Y01=0.7
X10=0.0
Y10=0.5
X00=0.5
Y00=0.1

x=np.zeros(n)
y=np.zeros(n)

for i in range(n-1):
    if (x[i]==1) and (y[i]==1): 
        if np.random.rand()<X11:
            x[i+1]=1
        if np.random.rand()<Y11:
            y[i+1]=1 
    elif x[i]==1:
        if np.random.rand()<X10:
            x[i+1]=1
        if np.random.rand()<Y01:
            y[i+1]=1
    elif y[i]==1:
        if np.random.rand()<X01:
            x[i+1]=1
        if np.random.rand()<Y10:
            y[i+1]=1          
            
    else:     
        if np.random.rand()<X00:
            x[i+1]=1
        if np.random.rand()<Y00:
            y[i+1]=1
        
print(" ".join(str(int(i)) for i in x))
print(" ".join(str(int(i)) for i in y))
        