# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:22:30 2020

@author: nnath
"""
import pandas as pd
import os

os.chdir(r'D:\GITHUB\PANDAS\Pandas')
os.listdir()
#read csv, delimiter is ','
df1 = pd.read_csv('example.csv',sep=",")
df1.head()
#to display column lables 
df1.columns
df1['Description']

#to replace junk values and to set index column
df11 = pd.read_csv('example.csv',index_col=0 ,na_values=["##","???"])
#to display row lables 
df11.index
                                                         
#import excel sheet
df2 = pd.read_excel('example.xlsx',sheet_name='sheet1',na_values=["##","???"])

                                                                  
#import txt file, delimiter is tab 
df3 = pd.read_table('example.txt', sep= "\t")
df3_1 = pd.read_table('example.txt', delimiter= "\t")                                                                  


#2 ways to copy
#shallow copy
sc  = df3.copy(deep=False)
#deep copy
dc  = df3.copy(deep=True)
