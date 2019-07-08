#!/usr/bin/env python
# coding: utf-8

# In[23]:


students = ["Ravi", "Chai", "Aniketh"]
print(students)


# In[5]:


print(students[2])


# In[6]:


print(students[0] + " & " + students[2] )


# In[8]:


print(len(students))


# In[9]:


students.append("Mani")
print(students)


# In[10]:


print(len(students))


# In[11]:


marks = [4,5,6,7,8]
print(marks)


# In[13]:


marks.append(2)
print(marks)


# In[14]:


print(len(marks))


# In[19]:


print((marks[0] + marks[1])/ len(marks))


# In[22]:


p = students.pop()
print(students)
print(p)


# In[24]:


print(students)


# In[26]:


last_student = students.pop()
print(last_student)
print(students)


# In[39]:


students = students + ["Aniketh"]
print(students)


# In[40]:


students.pop()
print(students)


# In[41]:


del students[2]
print(students)


# In[46]:


students.remove("Ravi")
print(students)


# In[45]:


students = students + ["Ravi"]
print(students)


# In[48]:


xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ys = [x * x for x in xs]
print (xs)
print (ys)


# In[50]:


ab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cd = []
for a in ab: cd.append(a * a)
print (ab)
print (cd)


# In[52]:


print(students)
lengths = [len(student) for student in students]
print(lengths)


# In[53]:


#drawing graphics
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

xaxis = [x/10 for x in range (0, 100)]
yaxis = [x*x for x in xaxis]

print(xaxis)
print(yaxis)

print(len(xaxis))
print(len(yaxis))

plt.plot(xaxis, yaxis)
plt.show()


# In[54]:


print(students)


# In[58]:


Nlist = [
    ["Ravi", "Chai", "Aniketh"],
    ["Krishna", "Latha"]
]
print(Nlist)
print(Nlist[1][1])


# In[ ]:




