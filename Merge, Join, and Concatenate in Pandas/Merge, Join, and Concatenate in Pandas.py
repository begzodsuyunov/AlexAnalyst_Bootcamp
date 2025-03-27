#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


df1 = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Merge, Join, and Concatenate in Pandas\LOTR.csv")
df1


# In[8]:


df2 = pd.read_csv(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Merge, Join, and Concatenate in Pandas\LOTR 2.csv")
df2


# In[14]:


#INNER join
df1.merge(df2)


# In[16]:


#INNER join
df1.merge(df2, how = 'inner')


# In[18]:


#INNER join
df1.merge(df2, how = 'inner', on = 'FellowshipID')


# In[20]:


#INNER join
df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])


# In[22]:


#OUTER JOIN
df1.merge(df2, how = 'outer')


# In[24]:


#LEFT JOIN
df1.merge(df2, how = 'left')


# In[26]:


#RIGHT JOIN
df1.merge(df2, how = 'right')


# In[28]:


#CROSS JOIN
df1.merge(df2, how = 'cross')


# In[30]:


df1.join(df2, on = 'FellowshipID', how ='outer', lsuffix = '_Left', rsuffix='_Right')


# In[36]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix='_Right', how = 'outer')
df4


# In[38]:


pd.concat([df1, df2])


# In[42]:


pd.concat([df1, df2], join = 'inner')


# In[44]:


pd.concat([df1, df2], join = 'outer', axis = 1)


# In[ ]:




