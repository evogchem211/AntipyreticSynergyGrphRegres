#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# In[26]:


yesBEN = []
yesASP =[]
for i in range(7):
    yesBEN.append(0.025)
for i in range(6):
    yesBEN.append(0.05)
for i in range(6):
    yesBEN.append(0.1)
for i in range(6):
    yesBEN.append(0.2)
for i in range(5):
    yesBEN.append(0.3)
for i in range(5):
    yesBEN.append(0.4)
for i in range(4):
    yesBEN.append(0.5)

axis = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1]
def runyes(run_num):
    for i in range(run_num):
         yesASP.append(axis[i])

runyes(7)
for i in range(3):
    runyes(6)
for i in range(2):
    runyes(5)
runyes(4)

axisnew = [1, 0.75, 0.5, 0.3, 0.2, 0.1, 0.05, 0.01]
noBEN =[]
noASP =[]
def run(run_num):
    for i in range(run_num):
         noASP.append(axisnew[i])


noBEN.append(0.025)
for i in range(2):
    noBEN.append(0.05)
for i in range(2):
    noBEN.append(0.1)
for i in range(2):
    noBEN.append(0.2)
for i in range(3):
    noBEN.append(0.3)
for i in range(3):
    noBEN.append(0.4)
for i in range(4):
    noBEN.append(0.5)


run(1)
for i in range(3):
    run(2)
for i in range(2):
    run(3)
run(4)

reg = LinearRegression()

uno = np.array([0.025, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]).reshape(-1, 1)
dos = np.array([1, 0.75, 0.75, 0.75, 0.5, 0.5, 0.3]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.intercept_, reg.coef_)


# In[28]:


Growth = plt.scatter(yesBEN, yesASP, c="r", label='Growth')
Inhibition = plt.scatter(noBEN, noASP, c="g", marker="x", label ='Inhibited')
plt.plot([0, 0.5], [0.91745283, 0.323113205], lw=3, c='black')
plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()
### y = -1.18867925x + 0.91745283


# In[ ]:




