# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:59:35 2021

@author: himanshu.k.bhesaniya
"""



#Using core python

#give csv path and output 
csv_path = 'D:\TEST\CodeTest\OrdersWithNulls.csv'
out_path = r'D:\TEST\CodeTest\Sample1.csv'

#function for extract required column
def mapfn(x):
     temp = x.strip().split(',')
     return temp[1], temp[3]

#Reading csv and get data
with open(csv_path, 'r') as file:
    data = file.readlines()[1:]
    cols = data[0]
    data = list(map(mapfn, data))

#Sorting data
sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
sorted_data.insert(0, cols)

#writing data as csv
with open(out_path, 'w') as out_file:
  for line in sorted_data:
    out_file.write(",".join(line) + "\n")

    
#------------------------------------------------------------
# Using external modules
#if you don't have this module install using command line 
# pip install pandas,os

#import required libraries
import os
import pandas as pd

#give root data path
root_dir = r'D:\TEST\CodeTest'
csv_path = os.path.join(root_dir,'OrdersWithNulls.csv')

#read csv file using pandas
df = pd.read_csv(csv_path)

#extract required columns
df = df[['Order Date','Sales']]

#sorting data
df = df.sort_values(by='Order Date', ascending=False)

#save as csv
df.to_csv(os.path.join(root_dir,'Sample.csv'), index=False)

