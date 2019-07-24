#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


#write a function to simulate the geometric brownian motion
def MCpaths(Nt, Np, mu, sigma, dt):
    dt=1/Nt
    paths=np.zeros((Nt+1,Np),np.float64)
    paths[0]=S0
    for t in range(1,Nt+1):
        rand=np.random.standard_normal(Np)
        paths[t]=paths[t-1]*np.exp((mu-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*rand)
    return paths


# In[142]:


S0=100     #the initial price
mu=0.1     #expected annual return
sigma=0.3  #standard deviation
Nt=252     #the number of time steps per path
Np=10000   #the number of paths
dt=1/Nt
plt.hist(paths[252],bins=50)
plt.title('Terminal value distribution')
plt.show()


# In[45]:


#the mean and standard deviation of the distribution:
terminal_v=pd.DataFrame(paths[252])
terminal_v.describe()


# In[175]:


#calculate the number of hitting or being across S0(the initial value)
count=0
for i in range(0,9999):
    for j in range(1,251):
        if ((y.iloc[j,i]<100)&(y.iloc[j+1,i]>=100))==1:
            count=count+1
        


# In[177]:


#The average number of the times that St hit or across the initial S0
count/10000


# In[201]:


#Consider a one-year European call option with strike price K=$100.
C=np.zeros((Nt+1,Np),np.float64)
for i in range(1,253):
    for j in range(1,10000):
        C[i,j]=max(paths[i,j]-100,0)
    


# In[202]:


#the mean terminal value of the payoff of that call option:
C_d=pd.DataFrame(C)
C_d.iloc[252:].values.mean()


# In[200]:


#As for the mean terminal value of the payoff of that put option:
P=np.zeros((Nt+1,Np),np.float64)
for t in range(1,253):
    for j in range(1,10000):
        P[t,j]=max(0,100-paths[t,j])
P_d=pd.DataFrame(P)
P_d.iloc[252:].values.mean()    #the mean terminal value of the put option


# In[98]:


import os
os.getcwd()
os.chdir('/Users/duanyihong/Desktop')
PS2=pd.read_excel('PS2data.xlsx',sep=',')
PS2


# In[100]:


PS2.x.describe()   #Mean and standard deviation of X 


# In[101]:


PS2.y.describe()    #Mean and standard deviation of Y 


# In[183]:


xi=PS2['x']
yi=PS2['y']
correlation=np.corrcoef(xi,yi)
correlation   #the correlation between x and y in the full sample is 0.817


# In[123]:


#the mean of x and y for seperate securityID
PS2.groupby('SecID').mean()


# In[124]:


#the std for seperate securityID
PS2.groupby('SecID').std()


# In[196]:


#the correlation of x and y
#np.correlate(PS2.groupby('SecID').x,PS2.groupby['SecID'].y)
CorID=PS2.groupby('SecID').apply(lambda x:np.corrcoef(x['x'],x['y']))


# In[197]:


CorID


# In[ ]:


#Discussion: the correlation coefficients between x and y is basically around the correlation coefficient
#between x and y in the full sample. It indicates that all of the securities contribute to the 
#whole correlation coefficient in the market

