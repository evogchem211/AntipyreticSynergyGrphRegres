#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[139]:


yesBEN =[]
yesACE =[]

axis = [0.1, 0.25, 0.75, 1, 1.5, 2, 2.5, 3]
for i in range(6):
    yesBEN.append(0.025)
for i in range(6):
    yesBEN.append(0.05)
for i in range(5):
    yesBEN.append(0.1)
for i in range(5):
    yesBEN.append(0.2)
for i in range(4):
    yesBEN.append(0.4)
for i in range(4):
    yesBEN.append(0.5)
    
def runyes(run_num):
    for i in range(run_num):
         yesACE.append(axis[i])

for i in range(2):
    runyes(6)
for i in range(2):
    runyes(5)
for i in range(2):
    runyes(4)

noBEN =[]
noACE =[]
axis.sort(reverse =True)
def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])
for i in range(2):
    noBEN.append(0.025)
for i in range(2):
    noBEN.append(0.05)
for i in range(3):
    noBEN.append(0.1)
for i in range(3):
    noBEN.append(0.2)
for i in range(4):
    noBEN.append(0.4)
for i in range(4):
    noBEN.append(0.5)

for i in range(2):
    run(2)
for i in range(2):
    run(3)
for i in range(2):
    run(4)


# In[142]:


### 0.65*-13.25^x + 4
def funct(x):
    a = np.log(x)
    b = -0.364*a
    final = b + 1.2586
    return(final)

ex = np.random.uniform(0.01, 0.5, 1000)
ex.sort()


# In[146]:


Growth =plt.scatter(yesBEN, yesACE, c="r", label="Growth")
Inhibition = plt.scatter(noBEN, noACE, c="g", marker="x", label='Inhibited')

for i in range(999):
    first =ex[i]
    second = ex[i+1]
    fig = plt.plot([first, second], [funct(first), funct(second)], lw=2, c="black")

plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()

### logathmic
### -0.364ln(x) + 1.2586


# In[ ]:




