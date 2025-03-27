#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Group by and Aggregating in Pandas\Flavors.csv")


# In[5]:


df


# In[7]:


group_by_frame = df.groupby('Base Flavor')


# In[21]:


group_by_frame.mean(numeric_only=True)


# In[23]:


group_by_frame.count()


# In[25]:


group_by_frame.min()


# In[27]:


group_by_frame.max()


# In[31]:


group_by_frame.agg({'Flavor Rating': ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum']})


# In[39]:


df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating': ['mean', 'max', 'count', 'sum']})


# In[41]:


group_by_frame.describe()


# In[ ]:




