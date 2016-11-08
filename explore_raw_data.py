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
def numeric_metrics(df = None, column_name = None, column_order_only = False):
    # Note: 
    #   Must update True segment if False segment is udpated
    if column_order_only:
        return_value = ['Mean', 'Range', 'Sd', 'Min', '25%', 'Median', '75%', 'Max']
    else:
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
                
        return_value = return_dict
        
    return return_value

def common_metrics(df = None, column_name = None, column_order_only = False):
    # Note: 
    #   Must update True segment if False segment is udpated
    if column_order_only:
        return_value = ['Column Name', 'Data Type', 'Count', '# of Uniques', '# of NaN', 'Smallest', 'Largest' ]
    else:   
        series = df[column_name]
        return_dict = {}
        return_dict['Column Name']  = column_name
        return_dict['Data Type']    = series.dtype
        return_dict['Count']        = len(series)
        return_dict['# of Uniques'] = series.nunique()
        return_dict['# of NaN']     = sum(pd.isnull(series))
        
        sorted_uniques = np.sort(series.unique())
        
        window_size = min(5, len(sorted_uniques))
        
        return_dict['Smallest'] = str(sorted_uniques[:window_size])
        return_dict['Largest']  = str(sorted_uniques[-window_size:])
        
        return_value = return_dict
    
    return return_value

def explore_columns(df):
    # By default, all columns are string now
    column_list = list(df.columns)
    column_order_for_export_2 = []
    return_list = []
    for column in column_list:
        temp_data = df[column]
        temp_dict = common_metrics(df, column)

        if (temp_data.dtype == 'int64') or (temp_data.dtype == 'float64'):
            temp_dict.update(numeric_metrics(df, column))
            column_order_for_export_2 = numeric_metrics(column_order_only = True)
            
        return_list.append(temp_dict)

    column_order_for_export = common_metrics(column_order_only = True) + column_order_for_export_2
    return pd.DataFrame(return_list), column_order_for_export
    
    
#%% 
if __name__ == '__main__':
    # Generic part
    data_df = pd.read_csv(r'example.csv', 
                          header = 0, 
                          low_memory = False, 
                          encoding = 'utf-8')
    
    data_description, data_column_order = explore_columns(data_df)
    
    # The folloing is example-spefic application
    column_description = pd.read_excel('LCDataDictionary.xlsx')
    column_description.rename(columns = {'LoanStatNew': 'Column Name'}, inplace = True)
    
    all_description = pd.merge(column_description, data_description, left_on = 'Column Name', 
                               right_on = 'Column Name', how = 'outer' )
    
    if False:
        all_description.to_csv('a.csv', columns = ['Description'] + data_column_order, encoding = 'utf-8')