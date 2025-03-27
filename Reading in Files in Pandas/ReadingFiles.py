#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[24]:


#Reading CSV file
df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Reading in Files in Pandas\countries of the world.csv", header = None, names = ['Country', 'Region'])
df


# In[26]:


#Reading TXT file
#df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Reading in Files in Pandas\countries of the world.txt", sep = '\t')
#df

df = pd.read_table(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Reading in Files in Pandas\countries of the world.txt", sep = '\t')
df


# In[50]:


#Reading JSON files
df = pd.read_json(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Reading in Files in Pandas\json_sample.json")
df


# In[52]:


#Reading EXCEL File
df2 = pd.read_excel(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Reading in Files in Pandas\world_population_excel_workbook.xlsx")
df2


# In[48]:


pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)


# In[56]:


df2.info()


# In[62]:


df2.shape


# In[64]:


df2.tail(10)


# In[66]:


df2.loc[224]


# In[ ]:




