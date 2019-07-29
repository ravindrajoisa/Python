#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = ["Ravi", "Aniketh", "Yoyo", "Dog", "Tri"]

last_student = students.pop()
print(last_student)
print(students)


# In[3]:


students = ["Ravi", "Aniketh", "Yoyo", "Dog", "Tri"] + ["Frank"]

print(students)


# In[6]:


students = ['Ravi', 'Aniketh', 'Yoyo', 'Dog', 'Tri', 'Frank']
del students[3]
print(students)


# In[7]:


students.remove('Frank')
print(students)


# In[ ]:




