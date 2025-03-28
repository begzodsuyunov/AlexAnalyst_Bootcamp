#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\PandasVisualization\Ice Cream Ratings.csv")
df.set_index('Date', inplace=True)
df


# In[55]:


print(plt.style.available)


# In[5]:


df.plot(kind = 'line', subplots = True)


# In[7]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[11]:


df.plot(kind = 'bar')


# In[13]:


df.plot(kind = 'bar', stacked = True)


# In[19]:


df['Flavor Rating'].plot(kind = 'bar', stacked = True)


# In[21]:


df.plot.barh(stacked = True)


# In[29]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'Yellow')


# In[35]:


df.plot.hist(bins = 10)


# In[37]:


df.boxplot()


# In[41]:


df.plot.area(figsize = (10,5))


# In[53]:


df.plot.pie(y = 'Flavor Rating', figsize = (8,8))


# In[ ]:




