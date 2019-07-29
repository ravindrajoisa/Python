#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello Ravi")


# In[2]:


def multi_print():
    print("Hello Aniketh")
    print("Hello Chaitra")


# In[3]:


multi_print()


# In[4]:


def multi_print2(name):
    print(name)
    print(name)
multi_print2("Krishna")
multi_print2("Latha")


# In[5]:


name = "Earth"

def multi_print2(name):
    print(name)
    print(name)

multi_print2("Krishna")
multi_print2("Latha")

print(name)


# In[6]:


print(len(["Hello", "Ravi"]))


# In[7]:


print(len("Ravindra"))


# In[8]:


def multi_print(name, count):
    for i in range(0, count):
        print(name)
        
multi_print("Hello", 4)


# In[9]:


#functions in functions

def another_func():
    multi_print("Hello!", 2)
    multi_print("Ravi", 3)
    
another_func()


# In[ ]:




