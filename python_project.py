#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

class Project:
    
    def __init__(self):
        # The csv file is stored in the same ddirectory as my jupyter notebook; 
        # calling is straight-forward
        self.data = pd.read_csv('python hands-on - dataset.csv')
        
    def isExpired(self): # Checks to see if any item is expired by comparing to the benchmark date '2021-01-01'
        self.data.loc[self.data['date'] >= '2021-01-01','obsolete'] = 'FALSE'
        self.data.loc[self.data['date'] < '2021-01-01','obsolete'] = 'TRUE'
        return self.data
        
    def toJson(self): #Plug in your local directory, mine is 'C:\\Users\\Kuz'
        with open("C:\\Users\\Kuz\\python-hands-on-dataset.json", "w+") as output_file: #Saving the file as json, filename is 'python-hands-on-dataset'
            output_file.write(self.data.to_json())

