#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = ["Aniketh", "Anika"]
students.append("Ravi")

print(students)


# In[8]:


class Students():
    pass

def get_name(student):
    print(student.firstname + " " + student.lastname)
    
abc = Students()
abc.firstname = "Ravindra"
abc.lastname = "Joisa"

xyz = Students()
xyz.firstname = "Aniketh"
xyz.lastname = "Joisa"

get_name(abc)
get_name(xyz)

#print(abc.firstname)
#print(abc.lastname)



# In[18]:


class Company():
    pass

def get_name(company):
    print(company.legal_name + " " + company.legal_type)
    
c = Company()
c.legal_name = "Joisa"
c.legal_type = "Ltd"

get_name(c)


# In[ ]:





# In[ ]:





# In[ ]:




