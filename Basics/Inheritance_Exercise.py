#!/usr/bin/env python
# coding: utf-8

# In[20]:


class FileReader():
    def __init__(self, filename):
        self.filename = filename
        
    def lines(self):
        lines = []
        with open(self.filename, "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines

    
class CsvReader(FileReader):
    def __init__(self,filename):
        super().__init__(filename)
        
    def lines(self):
        lines = super().lines()
   
    #     return(line.split(",") for line in lines)
        
        split_lines = []
        for line in lines: 
           split_lines.append(line.split(","))
        return split_lines


# In[21]:


f = FileReader("./file.csv")
print(f.lines())


# In[22]:


f = CsvReader("./file.csv")
print(f.lines())


# In[ ]:




