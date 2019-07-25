#!/usr/bin/env python
# coding: utf-8

# In[2]:


def multi_print(name, count):
    for i in range(0, count):
        print(name)
        
multi_print("Ravi", 4)


# In[3]:


def another_function():
    multi_print("Aniketh", 3)
    multi_print("Welcome", 2)


# In[4]:


another_function()


# In[6]:


def maximum(a,b):
    if a <b:
        return b
    else:
        return a
    
result = maximum(23,42)
print(result)


# In[ ]:




