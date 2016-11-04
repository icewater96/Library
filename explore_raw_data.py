# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 13:42:14 2016

@author: jllu
"""

# Explore a raw data table and generate report for each column
#   1) Determine where a column is TimeStamp, coninuous, continuous-categorical, discrete, or something else
#   2) Generate statis based on the column type
#   3) Provide example, histogram, number of blank or NaN

# TIP:
#   df.types
#   df.column.dtype
#   Only series and dataframe data types in Pandas: 'int64', 'float64', 'object', 'datetime64'


import pandas as pd
import numpy  as np


#%% 
def explore_columns(df):
    # By default, all columns are string now
    column_list = list(df.columns)
    
    report_list = []
    for column in column_list:
        temp_data = df[column]
        temp_dict = {}
        temp_dict['Column Name'] = column
        temp_dict['Data Type']   = temp_data.dtype

        if temp_data.dtype == 'int64':
            temp_dict['Min'] = min(temp_data)
            temp_dict['Max'] = max(temp_data)
            temp_dict['Mean'] = np.mean(temp_data)
            temp_dict['Median'] = np.median(temp_data)
            temp_dict['# of NaN'] = sum(np.isnan(df.id))
            temp_dict['Count'] = len(temp_data)
            temp_dict['# of Uniques'] = temp_data.nunique()
            sorted_uniques = np.sort(temp_data.unique())
            temp_dict['Smallest'] = str(sorted_unique.head(5))
            
        report_list.append(temp_dict)

#%% 
if __name__ == '__main__':
    # By default, all columns are string now
    df = pd.read_csv(r'D:\GitHub\Q\L_C\Data\LoanStats3b - trimmed.csv', 
                     header = 0, 
                     low_memory = False)