#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


# In[7]:


yesBEN =[]
yesACE = []

for i in range(5):
    yesBEN.append(0.025)
for i in range(5):
    yesBEN.append(0.05)
for i in range(5):
    yesBEN.append(0.1)
for i in range(4):
    yesBEN.append(0.15)
for i in range(4):
    yesBEN.append(0.2)
for i in range(3):
    yesBEN.append(0.3)

axis = [0.1, 0.25, 0.75, 1, 1.5, 1.75, 2, 2.5, 3]
def runyes(run_num):
    for i in range(run_num):
         yesACE.append(axis[i])

for i in range(3):
    runyes(5)
for i in range(2):
    runyes(4)
runyes(3)

noBEN =[]
noACE =[]
axis.sort(reverse=True)
def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])

for i in range(4):
    noBEN.append(0.025)
for i in range(4):
    noBEN.append(0.05)
for i in range(4):
    noBEN.append(0.1)
for i in range(5):
    noBEN.append(0.15)
for i in range(5):
    noBEN.append(0.2)
for i in range(6):
    noBEN.append(0.3)

for i in range(3):
    run(4)
for i in range(2):
    run(5)
run(6)

reg = LinearRegression()

uno = np.array([0.025, 0.05, 0.1, 0.15, 0.2, 0.3]).reshape(-1, 1)
dos = np.array([1.75, 1.75, 1.75, 1.5, 1.5, 1]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.coef_)
print(reg.intercept_)


# In[13]:


Growth = plt.scatter(yesBEN, yesACE, c="r", label='Growth')
Inhibition =plt.scatter(noBEN, noACE, c="g", marker="x", label='Inhibited')
plt.plot([0, 0.3], [1.91217565, 1.103792416], lw=2, c="black")
plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()
### -2.69461078x +1.91217565


# In[ ]:




