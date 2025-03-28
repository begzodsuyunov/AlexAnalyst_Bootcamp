#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_excel(r"D:\Self_Study\AlexTheAnalyst_YT\PY\Data Cleaning in Pandas\Customer Call List.xlsx")
df


# In[5]:


df = df.drop_duplicates()
df


# In[7]:


df = df.drop(columns = 'Not_Useful_Column')
df


# In[9]:


#df["Last_Name"]= df["Last_Name"].str.lstrip('...')
#df["Last_Name"]= df["Last_Name"].str.lstrip('/')
#df["Last_Name"]= df["Last_Name"].str.rstrip('_')
df["Last_Name"]= df["Last_Name"].str.strip('123./_')
df


# In[23]:


#df["Phone_Number"]=df["Phone_Number"].str.replace('[^a-zA-z0-9]', '', regex=True)
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' +x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' +x[3:6] + '-' + x[6:10])
df["Phone_Number"]=df["Phone_Number"].str.replace('[^a-zA-z0-9]', '', regex=True)


# In[25]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[:3] + '-' + x[3:6] + '-' + x[6:10] if len(x) == 10 else x)
df


# In[29]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan', '')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na', '')
df


# In[43]:


df[["Street Address", "State", "Zip_Code"]] = df['Address'].str.split(',', n = 2, expand=True)
df


# In[47]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df


# In[49]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[57]:


#df = df.replace('N/a', '')
#df = df.replace('NaN', '')
df = df.fillna('')
df


# In[59]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
df    


# In[77]:


#Dropping nulls
for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)

#Another way to drop null values
df.dropna(subset = "Phone_Number", inplace = True)
df


# In[79]:


df = df.reset_index(drop=True)
df


# In[ ]:




