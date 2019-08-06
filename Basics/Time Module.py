#!/usr/bin/env python
# coding: utf-8

# In[5]:


import time

ticks = time.time()
print(ticks)


# In[6]:


localtime = time.localtime(ticks)
print(localtime)


# In[7]:


# Getting formatted time

formattedtime = time.asctime(localtime)
print(formattedtime)


# In[8]:


import calendar

cal = calendar.month(2019, 7)
print(cal)


# In[ ]:




