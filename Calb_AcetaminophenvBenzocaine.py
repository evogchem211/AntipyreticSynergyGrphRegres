#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[19]:


yesBEN =[]
yesACE =[]
for i in range(5):
    yesBEN.append(0.05)
for i in range(5):
    yesBEN.append(0.1)
for i in range(5):
    yesBEN.append(0.2)
for i in range(5):
    yesBEN.append(0.3)
for i in range(4):
    yesBEN.append(0.4)

axis=[0.1, 0.25, 0.75, 1, 1.5, 2, 2.5, 2.75, 3]
def runyes(run_num):
    for i in range(run_num):
         yesACE.append(axis[i])
for i in range(4):
    runyes(5)

runyes(4)

noBEN =[]
noACE =[]
axis.sort(reverse=True)
def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])

for i in range(4):
    noBEN.append(0.05)
for i in range(4):
    noBEN.append(0.1)
for i in range(4):
    noBEN.append(0.2)
for i in range(4):
    noBEN.append(0.3)
for i in range(5):
    noBEN.append(0.4)     
for i in range(9):
    noBEN.append(0.5)

for i in range(4):
    run(4)
run(5)
run(9)

def funct(x):
    a= -65.493*pow(x, 3)
    b = 34.789*pow(x, 2)
    c = -5.2156*x
    final = a+b+c+2.2012
    return(final)

ex = np.random.uniform(0.01, 0.5, 1000)
ex.sort()


# In[23]:


Growth = plt.scatter(yesBEN, yesACE, c="r", label="Growth")
Inhibition = plt.scatter(noBEN, noACE, c="g", marker="x", label ="Inhibited")
plt.xlabel("Benzocaine concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
for i in range(999):
    first =ex[i]
    second = ex[i+1]
    fig = plt.plot([first, second], [funct(first), funct(second)], lw=2, c="black")
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()

### -65.493x^3 + 34.789x^2 - 5.2156x + 2.2012


# In[ ]:




