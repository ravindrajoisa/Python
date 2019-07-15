#!/usr/bin/env python
# coding: utf-8

# In[2]:


if True and False:
    print("Hello")   # Hello is not printed.


# In[3]:


if True or False:
    print("Hello")


# In[7]:


students = ["Ravi", "Havi", "Gavi", "Rovi"]
print("Ravi" in students)


# In[11]:


if "Gavi" in students:
    print("TomTom")
else:
    print ("NA")


# In[15]:


if "R0ovi" not in students:
    print("Bengali")
if not "Rovii" in students:
    print("Gujju")


# In[ ]:




