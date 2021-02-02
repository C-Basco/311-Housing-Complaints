#!/usr/bin/env python
# coding: utf-8

# In[6]:


# make sure to install these packages before running:
get_ipython().system(' pip install sodapy')


# In[12]:


#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
#https://data.cityofnewyork.us/resource/erm2-nwe9.json
results = client.get("erm2-nwe9", where="agency_name = 'Department of Housing Preservation and Development'", limit=2000)

# Convert to pandas DataFrame
DepHousing = pd.DataFrame.from_records(results)


# In[10]:


DepHousing.head(10)


# Taking dataframe and writing it into a csv file

# In[15]:


DepHousing.to_csv('HPD.csv')


# Reading `pluto_20v3.csv` into NYCPluto Dataframe using pandas

# In[16]:


NYCPluto = pd.read_csv('pluto_20v3.csv')


# In[17]:


print(NYCPluto)


# In[20]:


NYCPluto[NYCPluto.borough == 'MN']


# create a new dataframe with filtered data. The data will be filtered by borough. In this case it will be the borough of Manahttan. 

# In[21]:


NYCPluto = NYCPluto[NYCPluto.borough == 'MN']


# In[22]:


NYCPluto.to_csv('pluto_MN.csv')


# In[ ]:




