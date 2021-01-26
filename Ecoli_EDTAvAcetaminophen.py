#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[10]:


yesEDTA = [0.01, 0.01, 0.01, 0.01, 0.01, 0.025, 0.025, 0.025, 0.025, 0.05, 0.075, 0.075]
yesACE = [0.25, 0.2, 0.1, 0.05, 0.01, 0.2, 0.1, 0.05, 0.01, 0.01, 0.05, 0.01]
noEDTA = []
noACE = []
for i in range(6):
    noEDTA.append(0.01)
for i in range(7):
    noEDTA.append(0.025)
for i in range(7):
    noEDTA.append(0.05)
for i in range(9):
    noEDTA.append(0.075)
for i in range(11):
    noEDTA.append(0.1)
for i in range(11):
    noEDTA.append(0.2)
for i in range(11):
    noEDTA.append(0.25)
for i in range(11):
    noEDTA.append(0.5)
for i in range(11):
    noEDTA.append(1)

axis = [2.75, 2.5, 2.25, 1.75, 1.25, 0.5, 0.25, 0.2, 0.1, 0.05, 0.01]
def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])

run(6)
run(7)
run(7)
run(9)
for i in range(5):
    run(11)

reg = LinearRegression()

uno = np.array([0.01, 0.025, 0.05, 0.075, 0.1]).reshape(-1, 1)
dos = np.array([0.5, 0.25, 0.25, 0.1, 0.01]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.intercept_, reg.coef_)


# In[16]:


Growth =plt.scatter(yesEDTA, yesACE, c="r", label='Growth')
Inhibition = plt.scatter(noEDTA, noACE, c="g", marker="x", label='Inhibited')
fig = plt.plot([0, 0.0984570073], [0.4704878, 0], lw=2, c="black")
plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()


# In[ ]:


### y = -4.77861163x +0.4704878

