#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Exploratory Data Analysis in Pandas\world_population.csv")
df


# In[6]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[8]:


df


# In[10]:


df.info()


# In[12]:


df.describe()


# In[16]:


df.isnull().sum()


# In[20]:


df.nunique()


# In[30]:


df.sort_values(by="2022 Population", ascending = False).head(4)


# In[34]:


df.corr(numeric_only = True)


# In[64]:


sns.heatmap(df.corr(numeric_only = True), annot = True)

plt.rcParams['figure.figsize'] = (20,7)
plt.show()


# In[77]:


df.groupby('Continent').mean(numeric_only=True).sort_values(by = "2022 Population", ascending = False)


# In[73]:


df[df['Continent'].str.contains('Oceania')]


# In[101]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by = "2022 Population", ascending = False)
#OR
#df2 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only=True).sort_values(by = "2022 Population", ascending = False)
df2


# In[103]:


df.columns


# In[105]:


df3 = df2.transpose()


# In[107]:


df3.plot()


# In[117]:


df.boxplot(figsize=(20,10))


# In[127]:


df.dtypes


# In[129]:


df.select_dtypes(include = 'object')


# In[131]:


df.select_dtypes(include = 'float')


# In[ ]:




