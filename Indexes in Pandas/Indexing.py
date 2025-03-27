#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[62]:


df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Indexes in Pandas\world_population.csv", index_col ='Country')
df


# In[68]:


df.reset_index(inplace=True)
df


# In[70]:


df.set_index('Country', inplace = True)
df


# In[72]:


df.loc['Albania']


# In[74]:


df.iloc[1]


# In[76]:


df.reset_index(inplace = True)


# In[78]:


df.set_index(['Continent', 'Country'], inplace = True)


# In[82]:


pd.set_option('display.max.columns', 40)
pd.set_option('display.max.rows', 235)


# In[129]:


population_columns = [
    "2022 Population", "2020 Population", "2015 Population", "2010 Population",
    "2000 Population", "1990 Population", "1980 Population", "1970 Population"
]

# Round and convert to integer
df[population_columns] = df[population_columns].astype(str)

float_columns_to_convert = [
    "Area (km²)", "Density (per km²)", "Growth Rate", "World Population Percentage"
]

df[float_columns_to_convert] = df[float_columns_to_convert].astype(str)


# In[131]:


df.sort_index(ascending=False)


# In[ ]:




