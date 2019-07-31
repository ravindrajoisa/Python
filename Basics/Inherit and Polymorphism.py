#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.term = 1
        
    def name(self):
        return self.firstname + " " + self.lastname
    
class WorkingStudent(Student):                                  # Student is from the super class >> inherit
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)                   # using super() to inherit
        self.company = company
    
#    def name(self):
#        return "WorkingStudent:" + self.firstname + " " + self.lastname      #this will overwrite the method in the super class

    def name(self):
        return super().name() + " (" + self.company + ")"       # want to add something in addition to what is present in super method.
    
student = [
    WorkingStudent("Ravi", "Joisa", "EMC"),
    Student("Chai", "V"),
    Student("Ani", "Kid"),
    WorkingStudent("Latha", "Krishna", "Home") 
]
                                                                #polymorphism
for stud in student:
    print(stud.name())


# In[ ]:





# In[ ]:




