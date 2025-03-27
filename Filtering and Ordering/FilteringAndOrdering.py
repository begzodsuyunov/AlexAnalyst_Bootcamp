#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[8]:


df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Filtering and Ordering\world_population.csv")


# In[10]:


df


# In[12]:


df[df['Rank'] < 10]


# In[14]:


specific_countries = ['Brazil', 'China']

df[df['Country'].isin(specific_countries)]


# In[22]:


df[df['Country'].str.contains('United')]


# In[26]:


df2 = df.set_index('Country')
df2


# In[36]:


df2.filter(items = ['Continent', 'CCA3'], axis = 1)


# In[40]:


df2.filter(items = ['Zimbabwe'], axis = 0)


# In[46]:


df2.filter(like = 'United', axis = 0)


# In[48]:


df2.loc['United States']


# In[50]:


df2.iloc[3]


# In[56]:


df[df['Rank'] < 10].sort_values(by=['Rank', 'Country'], ascending=[False, True])


# In[ ]:




