#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Car:
    price = "expensive"
    
c = Car
print(c.price)


# In[3]:


c.price = "cheap"
print(c.price)


# In[4]:


bobbycar = Car
print(bobbycar.price)


# In[9]:


class CarI:
    color = "blue"               #static variable and cannot be changed in a constructor.
    def __init__(self, price):
        self.price = price
        
c = CarI("jo")
print(c.price)
print(c.color)

d = CarI("bo")
print(d.price)
print(d.color)


# In[ ]:




