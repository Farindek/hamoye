#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url='https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data.describe(include='all')


# In[2]:


#Question 6
fuel_data.isnull().sum()


# In[14]:


fuel_data.corr().loc[('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[55]:


yearly_costs = fuel_data.groupby("report_year")["fuel_cost_per_unit_burned"].mean()
yearly_costs


# In[ ]:





# In[53]:


fuel_data.iloc[0:75].reset_index(drop=True)


# In[26]:


import numpy as np
a = np.array(['fuel_mmbtu_per_unit'])
p = np.percentile(a,75)


# In[42]:


fuel_data.groupby('report_year')['report_year'].count()


# In[21]:


fuel_data.corr().loc["fuel_cost_per_unit_burned"].sort_values()


# In[57]:


fuel_data.groupby('report_year')['fuel_cost_per_unit_burned'].sum()


# In[16]:


#Question5
fuel_data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[43]:


#question6
fuel_data.groupby('report_year')['fuel_mmbtu_per_unit'].std()


# In[62]:


A = fuel_data.groupby('report_year')['fuel_mmbtu_per_unit']
B = (A, P=75)
B


# In[13]:


print(pd.DataFrame())


# In[11]:


#Question 1
AList = [1,2,3,4,5,6]
BList = [13, 21, 34]
AList.extend(BList)
AList


# In[64]:


sns.heatmap(fuel_data.corr(), annot=True, fmt='.0%')


# In[ ]:




