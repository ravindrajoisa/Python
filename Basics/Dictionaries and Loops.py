#!/usr/bin/env python
# coding: utf-8

# In[12]:


d = {"India": "IND", "England": "ENG", "United States": "USA"}

for key in d:
    value = d[key]
    print(key)
    print(value)
    
print(d.items())


# In[13]:


for key, value in d.items():
    print(key + ":" + value)


# In[ ]:




