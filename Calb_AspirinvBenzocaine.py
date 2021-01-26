#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[5]:


yesASP =[]
yesBEN =[]

for i in range(3):
    yesBEN.append(0.05)
for i in range(2):
    yesBEN.append(0.1)
for i in range(2):
    yesBEN.append(0.2)
for i in range(2):
    yesBEN.append(0.3)
yesBEN.append(0.4)
axis = [0.05, 0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5]
def runyes(run_num):
    for i in range(run_num):
         yesASP.append(axis[i])
runyes(3)
for i in range(3):
    runyes(2)
runyes(1)

noASP =[]
noBEN =[]
axis.sort(reverse=True)
def run(run_num):
    for i in range(run_num):
         noASP.append(axis[i])
for i in range(5):
    noBEN.append(0.05)
for i in range(6):
    noBEN.append(0.1)
for i in range(6):
    noBEN.append(0.2)
for i in range(6):
    noBEN.append(0.3)
for i in range(7):
    noBEN.append(0.4)
for i in range(8):
    noBEN.append(0.5)

run(5)
for i in range(3):
    run(6)
run(7)
run(8)

reg = LinearRegression()

uno = np.array([0.05, 0.1, 0.2, 0.3, 0.4, 0.5]).reshape(-1, 1)
dos = np.array([0.5, 0.25, 0.25, 0.25, 0.1, 0.05]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.coef_)
print(reg.intercept_)


# In[9]:


Growth =plt.scatter(yesBEN, yesASP, c="r", label="Growth")
Inhibition =plt.scatter(noBEN, noASP, c="g", marker="x", label="Inhibited")
plt.plot([0, 0.55], [0.44, 0], lw = 2, c="black")
plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()
### y = -0.8x + 0.44


# In[ ]:




