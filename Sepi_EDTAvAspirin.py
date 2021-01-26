#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[16]:


yesEDTA =[0.01, 0.01, 0.05]
yesASP =[0.025, 0.01, 0.01]
noEDTA =[]
noASP =[]

for i in range(5):
    noEDTA.append(0.01)
for i in range(6):
    noEDTA.append(0.05)
for i in range(7):
    noEDTA.append(0.075)
for i in range(7):
    noEDTA.append(0.1)
for i in range(7):
    noEDTA.append(0.2)

axis = [1, 0.75, 0.5, 0.25, 0.1, 0.025, 0.01]
def run(run_num):
    for i in range(run_num):
         noASP.append(axis[i])

run(5)
run(6)
for i in range(3):
    run(7)
    

reg = LinearRegression()

uno = np.array([0.01, 0.05, 0.075]).reshape(-1, 1)
dos = np.array([0.1, 0.025, 0.01]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.intercept_, reg.coef_)


# In[18]:


Growth = plt.scatter(yesEDTA, yesASP, c="r", label='Growth')
Inhibition = plt.scatter(noEDTA, noASP, c="g", marker="x", label ='Inhibition')
fig = plt.plot([0, 0.0764634179], [0.10936047, 0], lw=2, c="black")
plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()


# In[ ]:


### y = -1.43023256x + 0.10936047

