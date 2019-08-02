#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname
        
class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)
        self.company = company
        
    def name(self):
        return super().name() + " (" + self.company + ")"


# In[5]:


w_student = WorkingStudent("John", "Doa", "Evilcorp")
student = Student("Monica", "Miller")


# In[8]:


print(type(w_student))
print(type(student))

if type(student) == Student:
    print("For Non Working student only")
elif type(w_studdent) == WorkingStudent:
    print("Foe Working student only")


# In[11]:


print(isinstance(w_student, WorkingStudent))
print(isinstance(student, WorkingStudent))
print(isinstance(w_student, Student)) #takes inheritance into consideration, while type doesn't.


# In[ ]:




