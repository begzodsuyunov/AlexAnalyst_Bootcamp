#!/usr/bin/env python
# coding: utf-8

# In[140]:


from bs4 import BeautifulSoup
import requests


# In[142]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


# In[144]:


world_titles = table.find_all('th')


# In[162]:


table = soup.find_all('table')[0]
print(table)


# In[164]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[166]:


import pandas as pd


# In[168]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[170]:


column_data = table.find_all('tr')
print(column_data)


# In[172]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[174]:


df


# In[176]:


df.to_csv(r'D:\Self_Study\AlexTheAnalyst_YT\PY\Scraping Data from a Real Website\Companies.csv', index = False)


# In[ ]:




