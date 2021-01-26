#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# In[10]:


yesASP = []
yesEDTA = []
axis = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.5, 1]

def runyes(run_num):
    for i in range(run_num):
         yesASP.append(axis[i])
for i in range(6):
    yesEDTA.append(0.01)
for i in range(6):
    yesEDTA.append(0.025)
for i in range(6):
    yesEDTA.append(0.05)
for i in range(5):
    yesEDTA.append(0.1)

for i in range(3):
    runyes(6)
runyes(5)

axis.sort(reverse=True)

def run(run_num):
    for i in range(run_num):
         noASP.append(axis[i])

noASP = []
noEDTA = []

for i in range(2):
    noEDTA.append(0.01)
for i in range(2):
    noEDTA.append(0.025)
for i in range(2):
    noEDTA.append(0.05)
for i in range(3):
    noEDTA.append(0.1)
for i in range(8):
    noEDTA.append(0.2)

for i in range(3):
    run(2)
run(3)
run(8)

reg = LinearRegression()

uno = np.array([0.01, 0.025, 0.05, 0.1, 0.2]).reshape(-1, 1)
dos = np.array([0.5, 0.5, 0.5, 0.25, 0.01]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.coef_)
print(reg.intercept_)


# In[15]:


Growth = plt.scatter(yesEDTA, yesASP, c="r", label = "Growth")
Inhibition = plt.scatter(noEDTA, noASP, c="g", marker="x", label="inhibited")
plt.plot([0, 0.2027219], [0.56758694, 0], lw = 2, c="black")
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.show()
### y = -2.79983036x + 0.56758694


# In[ ]:




