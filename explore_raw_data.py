# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 13:42:14 2016

@author: jllu
"""

# Explore a raw data table and generate report for each column
#   1) Determine where a column is TimeStamp, coninuous, continuous-categorical, discrete, or something else
#   2) Generate statis based on the column type
#   3) Provide example, histogram, number of blank or NaN

import pandas as pd
import numpy  as np


#%% 
def explore_columns(df):
    # By default, all columns are string now
    column_list = list(df.columns)
    
    #for column in column_list:
                



#%% 
if __name__ == '__main__':
    # By default, all columns are string now
    df = pd.read_csv(r'D:\GitHub\Q\L_C\Data\LoanStats3b - trimmed.csv', 
                     header = 0, 
                     low_memory = False)