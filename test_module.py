#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

class UnitTest:
    def __init__(self): # The csv file is stored in the same ddirectory as my jupyter notebook; 
        #calling is straight-forward
        self.data_test = pd.read_csv('python hands-on - dataset.csv')
    
    # The assumption is that each identifier(sku) is unique; so we check to affrim that there are no duplicates
    def no_duplicates(self):
        if len(self.data_test['sku'].unique()) == self.data_test.shape[0]:
            return True
        return False
    
    #Checking to see that the csv file read into the dataframe correctly 
    def read_file_correctly(self):
        if not self.data_test.empty:
            return True
        return False
    
    #Checking to see that there's no n/a value
    def no_missing_values(self):
        return list(self.data_test[self.data_test.columns].isna().sum()) == len(self.data_test.columns)*[0]
    
    

