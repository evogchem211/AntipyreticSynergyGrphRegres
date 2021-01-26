#!/usr/bin/env python
# coding: utf-8

# In[31]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# In[44]:


yesEDTA = [0.01, 0.01, 0.01, 0.01, 0.01, 0.025, 0.025]
yesASP = [0.2, 0.15, 0.1, 0.05, 0.01, 0.05, 0.01]
noEDTA = []
for i in range(6):
    noEDTA.append(0.01)
for i in range(9):
    noEDTA.append(0.025)
for i in range(11):
    noEDTA.append(0.05)
for i in range(11):
    noEDTA.append(0.075)
for i in range(11):
    noEDTA.append(0.1)
for i in range(11):
    noEDTA.append(0.2)
for i in range(11):
    noEDTA.append(0.5)
noASP = []

axis = [1.75, 1.25, 1, 0.75, 0.5, 0.25, 0.2, 0.15, 0.1, 0.05, 0.01]
def run(run_num):
    for i in range(run_num):
         noASP.append(axis[i])

run(6)
run(9)
for i in range(5):
    run(11)

reg = LinearRegression()

uno = np.array([0.01, 0.025, 0.05]).reshape(-1, 1)
dos = np.array([0.25, 0.1, 0.01]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.intercept_, reg.coef_)


# In[57]:


Growth = plt.scatter(yesEDTA, yesASP, color="r", label='Growth')
Inhibition = plt.scatter(noEDTA, noASP, color="g", marker="x", label="Inhibited")
fig = plt.plot([0, 0.0491843964], [0.28306122, 0], lw=2, c="black")
plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()


# In[46]:


### -5.75510204x + 0.28306122

