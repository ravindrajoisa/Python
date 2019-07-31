#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Students():
    def __init__(self, firstname, lastname, term):
        self.firstname = firstname
        self.lastname = lastname
        self.term = term
    
    def increase_term(self):
        self.term += 1
    
    def get_name(self):
        print(self.firstname + " " + self.lastname + " Semester is " + str(self.term))
    
abc = Students("Ravindra", "Joisa", 2)
abc.increase_term()
abc.get_name() 
#abc.firstname = "Ravindra"
#abc.lastname = "Joisa"

xyz = Students("Aniketh", "Joisa", 4)
xyz.get_name()
#xyz.firstname = "Aniketh"
#xyz.lastname = "Joisa"

#get_name(abc)
#get_name(xyz)


# In[ ]:





# In[ ]:




