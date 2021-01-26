#!/usr/bin/env python
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# In[40]:


yesASP =[]
yesBEN =[]

for i in range(4):
    yesBEN.append(0.05)
for i in range(3):
    yesBEN.append(0.1)
for i in range(2):
    yesBEN.append(0.25)
for i in range(2):
    yesBEN.append(0.5)

yesBEN.append(0.75)


axis = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.75]

def runyes(run_num):
    for i in range(run_num):
         yesASP.append(axis[i])

runyes(4)
runyes(3)
for i in range(2):
    runyes(2)
runyes(1)

noASP= []
noBEN =[]

axis.sort(reverse=True)
def run(run_num):
    for i in range(run_num):
         noASP.append(axis[i])

for i in range(3):
    noBEN.append(0.05)
for i in range(4):
    noBEN.append(0.1)
for i in range(5):
    noBEN.append(0.25)
for i in range(5):
    noBEN.append(0.5)
for i in range(6):
    noBEN.append(0.75)
for i in range(7):
    noBEN.append(1)
            
run(3)
run(4)
for i in range(2):
    run(5)
run(6)
run(7)

reg = LinearRegression()

uno = np.array([0.05, 0.1, 0.25, 0.5, 0.75, 1]).reshape(-1, 1)
dos = np.array([1, 0.75, 0.5, 0.5, 0.25, 0.1]).reshape(-1, 1)

reg.fit(uno, dos)
print(reg.coef_)
print(reg.intercept_)


# In[44]:


Growth = plt.scatter(noBEN, noASP, c='g', marker="x", label='Growth')
Inhibition = plt.scatter(yesBEN, yesASP, c="r", label='Inhibited')
plt.plot([0, 1.078617487], [0.87492737, 0], lw = 2, c="black")
plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Aspirin concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()
### y = -0.8111563x + 0.87492737


# In[ ]:




