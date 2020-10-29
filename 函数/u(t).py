# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
def step_function1(x=''):
    if x >0:
        return 1
    else:
        return 0

def step_function2(x):

    y = x > 0  
    return y.astype(np.int)   

m = 1
print(step_function1(m))

x = np.arange(-5.0,5.0,0.1)  
y = step_function2(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.xlabel('t')
plt.ylabel('u(t)')
plt.show()