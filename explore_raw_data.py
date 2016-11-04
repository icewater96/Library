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
def numeric_metrics(df, column_name):
    series = df[column_name]
    description = df[column_name].describe()
    return_dict = {}
    return_dict['Min']          = description['min']
    return_dict['Max']          = description['max']
    return_dict['Mean']         = description['mean']
    return_dict['25%']          = description['25%']
    return_dict['Median']       = description['50%']
    return_dict['75%']          = description['75%']
    return_dict['Range']        = return_dict['Max'] - return_dict['Min']
    return_dict['Sd']           = description['std']
    return_dict['# of NaN']     = sum(np.isnan(series))

    return return_dict

def common_metrics(df, column_name):
    series = df[column_name]
    return_dict = {}
    return_dict['Column Name']  = column_name
    return_dict['Data Type']    = series.dtype
    return_dict['Count']        = len(series)
    return_dict['# of Uniques'] = series.nunique()
    
    sorted_uniques = np.sort(series.unique())
    
    window_size = min(5, len(sorted_uniques))
    
    return_dict['Smallest'] = str(sorted_uniques[:window_size])
    return_dict['Largest']  = str(sorted_uniques[-window_size:])
    
    return return_dict

def explore_columns(df):
    # By default, all columns are string now
    column_list = list(df.columns)
    
    return_list = []
    for column in column_list:
        temp_data = df[column]
        temp_dict = common_metrics(df, column)

        if (temp_data.dtype == 'int64') or (temp_data.dtype == 'float64'):
            temp_dict.update(numeric_metrics(df, column))
            
        return_list.append(temp_dict)

    return pd.DataFrame(return_list)
    
    
#%% 
if __name__ == '__main__':
    # By default, all columns are string now
    df = pd.read_csv(r'example.csv', 
                     header = 0, 
                     low_memory = False)
    
    
    column_description = explore_columns(df)
    
    if False:
        column_description.to_csv('a.csv')