#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[17]:


yesACE = []
yesEDTA = []

def runyes(run_num):
    for i in range(run_num):
         yesACE.append(axis[i])

axis = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 1, 1.5, 2]

for i in range(7):
    yesEDTA.append(0.01)
for i in range(7):
    yesEDTA.append(0.025)
for i in range(6):
    yesEDTA.append(0.05)
for i in range(5):
    yesEDTA.append(0.1)

for i in range(2):
    runyes(7)
runyes(6)
runyes(5)

def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])
noACE = []
noEDTA =[]
axis.sort(reverse=True)
for i in range(3):
    noEDTA.append(0.01)
for i in range(3):
    noEDTA.append(0.025)
for i in range(4):
    noEDTA.append(0.05)
for i in range(5):
    noEDTA.append(0.1)
for i in range(10):
    noEDTA.append(0.2)
for i in range(2):
    run(3)
run(4)
run(5)
run(10)

def funct(x):
    a= -24.58*x
    b = 1.7433*np.exp(a)
    final = b+0.1
    return(final)

ex = np.random.uniform(0.01, 0.2, 1000)
ex.sort()


# In[24]:


Growth = plt.scatter(yesEDTA, yesACE, c="r", label="Growth")
Inhibition = plt.scatter(noEDTA, noACE, c="g", marker="x", label ='Inhibited')
plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
for i in range(999):
    first =ex[i]
    second = ex[i+1]
    fig = plt.plot([first, second], [funct(first), funct(second)], lw=2, c="black")
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()


# In[ ]:


### (1.7433*e^-24.58x) +0.1

