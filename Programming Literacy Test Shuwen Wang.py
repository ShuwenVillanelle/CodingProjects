#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import os 
import random 
import matplotlib.pyplot as plt


# In[2]:


os.chdir('/Users/duanyihong/Desktop')


# In[3]:


data=pd.read_csv('ProgrammingLiteracyTest.csv')


# In[4]:


data


# In[52]:


def Randomwalk(T,sigma,x0):
    paths=np.zeros((T+1,1),np.float64)
    paths[0]=x0
    for t in range(1,T+1):
        rand=random.uniform(0,1)
        if rand>0.5:
            ipsilon=1
        else:
            ipsilon=-1
        paths[t]=paths[t-1]+sigma*ipsilon
    return paths


# In[53]:


RW=Randomwalk(60,0.1,1)
plt.plot(RW)
plt.xlabel('Time')
plt.ylabel('Price_RW')
plt.show()


# In[49]:


data['M_inflation']=(data['CPIAUCSL']-data['CPIAUCSL'].shift(1))/data['CPIAUCSL'].shift(1)
df=np.split(data,2)


# In[30]:


df[0]


# In[31]:


df[1]


# In[38]:


df[0].describe()
mean1=df[0]['M_inflation'].mean()
mean1


# In[36]:


df[1].describe()
mean2=df[1]['M_inflation'].mean()
mean2


# In[42]:


plt.plot(data['DATE'],data['M_inflation'])
plt.xlabel('Time')
plt.ylabel('M_inflation')
plt.axhline(mean1,color='red',linestyle='--')
plt.axhline(mean2,color='green',linestyle='--')
plt.show()

