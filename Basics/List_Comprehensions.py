#!/usr/bin/env python
# coding: utf-8

# In[1]:


xs = [1,2,3,4,5,6,7,8]

ys = []
for x in xs:
    ys.append(x*x)
    
print(xs)
print(ys)


# In[2]:


xs = [1,2,3,4,5,6,7,8]

ys = [x*x for x in xs]

print(xs)
print(ys)


# In[4]:


students = ["Max", "Min", "Xi", "Feng", "Ding"]

#lengths = []
#for student in students:
#    lengths.append(len(student))

lengths = [len(student) for student in students]

print(lengths)


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt



plt.plot(xs, ys)
plt.show


# In[ ]:




