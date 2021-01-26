#!/usr/bin/env python
# coding: utf-8

# In[233]:


import numpy as np
import matplotlib.pyplot as plt


# In[228]:


yesEDTA = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.05]
yesACE = [2.5, 2.25, 1.75, 1.25, 0.5, 0.25, 0.25]

noEDTA = []
noACE = []

for i in range(5):
    noEDTA.append(0.05)
for i in range(6):
    noEDTA.append(0.075)
for i in range(6):
    noEDTA.append(0.1)
for i in range(6):
    noEDTA.append(0.2)
    
axis = [2.5, 2.25, 1.75, 1.25, 0.5, 0.25]
def run(run_num):
    for i in range(run_num):
         noACE.append(axis[i])
            
run(5)
for i in range(3):
    run(6)


# In[229]:


ex = np.random.uniform(0.025, 0.2, 1000)

ex.sort() 


# In[230]:


### 7.90569415*1e-20^x 
def funct(x):
    a = 1*(10**-20)
    c = pow(a, x)
    final = c*7.90569415
    return(final)

print(ex[0])

funct(ex[0])

### 7.90569415*(1*10^-20)^x


# In[235]:


Growth =plt.scatter(yesEDTA, yesACE, c="r", label="Growth")
Inhibition = plt.scatter(noEDTA, noACE, c="g", marker="x", label ='Inhibition')

for i in range(999):
    first =ex[i]
    second = ex[i+1]
    fig = plt.plot([first, second], [funct(first), funct(second)], lw=2, c="black")

plt.xlabel("EDTA concentration(mg/ml)", fontsize = 12)
plt.ylabel("Acetaminophen concentration(mg/ml)", fontsize = 12)
plt.legend(handles=[Growth, Inhibition], loc='upper right')
plt.show()


# In[ ]:




