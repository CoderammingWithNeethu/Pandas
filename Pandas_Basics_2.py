# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:22:30 2020

@author: nnath
"""
import pandas as pd
import os
import numpy as np

os.chdir(r'D:\GITHUB\PANDAS\Pandas')
os.listdir()
#read csv, delimiter is ','
df1 = pd.read_csv('example.csv',sep=",")
df1.head()#default is 5 rows
df1.head(10)
#to display column lables 
df1.columns
df1.size#number of elelments in df
df1['Description']
df1.memory_usage()

#to replace junk values and to set index column
df11 = pd.read_csv('example.csv',index_col=0 ,na_values=["##","???"])
#to display row lables 
df11.index
                                                         
#import excel sheet and remove special characters
df2 = pd.read_excel('example.xlsx',sheet_name='sheet1',na_values=["##","???"])

                                                                  
#import txt file, delimiter is tab 
df3 = pd.read_table('example.txt', sep= "\t")
df3_1 = pd.read_table('example.txt', delimiter= "\t")                                                                  


#2 ways to copy
#shallow copy
sc  = df3.copy(deep=False)
#deep copy; 
dc  = df3.copy(deep=True)
#slicing and indexing 
#at-->label-based lookup
#iat-->integer-based lookup
df1.at[4,'Revised']#4th row , Revised column data
df1.iat[4,2]#4th row, 2nd column
#to access groups of rows and columns by label .loc[]
df1.loc[2:10,'Period'] #row index from 2nd to 10th of 'Period' column


#DATA TYPES
df1.dtypes
df1.get_dtype_counts()#group by dtypes and return count of columns
df1.select_dtypes(exclude=[object])#to select specific data type of columns
df1.select_dtypes(exclude=[object]).columns
df1.select_dtypes(include=[object])
df1.select_dtypes(include=[object]).columns
df1.info()#summary of dataframe
#unique/distinct values of particular column
np.unique(df1['Period'])
pd.unique(pd.Series(df1['Period']))
pd.unique(df1['Period'])
#convert datatype of the column
df1_test = df1
df1_test['Revised'] = df1_test['Revised'].astype('object')
df1_test.dtypes

#bytes consumed
df1['Revised'].nbytes
df1['Revised'].astype('category').nbytes#checking if datatype was 'category' then bytes consumed would be what
#replace old value with new value 
df1_test['Period'].replace(2020.06,2222.2,inplace=True)
pd.unique(df1_test['Period'])
#how many are null values
df1.isnull().sum()
df1_test.loc[:2,'Period'].replace(2222.2,0)
df1_test['Period']=df1_test['Period'].astype('object')
df1_test.loc[:2,'Period'].fillna('No data',inplace=True)#fills nan value with 'No data'
df1_test.loc[:2,'Period'].replace(2222.2, np.nan,inplace=True)#convert particular dataset to Nan
df1_test.loc[10:15,'Period'].replace({2222.2: None},inplace=True)#convert particular dataset to None
df1_test.isnull().sum()#gives count of Nan values in each column


#insert a new column
df1.insert(2,'new_column','')#new column at index 2 with blank values
#drop the column
df1=df1.drop(columns=['new_column'])
df1.columns

#convert dataframe to csv
df1.to_csv(r'D:\GITHUB\PANDAS\Pandas\df1_test.csv',index = False)

#sorting on the column
df1.sort_values(['Revised'],ascending=[1])
df1.sort_values(['Revised','Previously published'],ascending=[1,0])

df1.describe()#statistice information column wise in a dataframe 

#AGGREGATE FUNCTION
df1['count']=1
df1.groupby(['Revised','Previously published']).count()['count']
df1.groupby(['Revised','Previously published']).count()['count'].reset_index()#normalised form

#EXPLORATORY DATA ANALYSIS
#Cross Tabulation
pd.crosstab(index=df1['Revised'],columns='count',dropna=True)#similar to group by

pd.crosstab(index=df1['Revised'],columns=df1['Previously published'],dropna=True)

#2-Way table : joint probability; is likelihood of two independent event happening at the same time
pd.crosstab(index=df1['Revised'],columns=df1['Previously published'],normalize = True ,dropna=True)
pd.crosstab(index=df1['Revised'].head(5),columns=df1['Previously published'].head(5),normalize = True ,dropna=True)

#2-way table : marginal probability; probability of occurrence of single event
pd.crosstab(index=df1['Revised'].head(5),columns=df1['Previously published'].head(5),margins = True, normalize = True ,dropna=True)

#2-way table : conditional probability ; probaility of event A given that another event B has already occured
#row wise; rows wise sum =1
pd.crosstab(index=df1['Revised'].head(5),columns=df1['Previously published'].head(5),normalize = 'index',margins = True ,dropna=True)
#column wise -- column wise sum = 1 
pd.crosstab(index=df1['Revised'].head(5),columns=df1['Previously published'].head(5),normalize = 'columns',margins = True ,dropna=True)


#CORRELATION : Pearson's correlation:strength of association between 2 variables ; 
#excluding null and categorial variables 
numerical_data =df1.select_dtypes(exclude=[object])
numerical_data.shape
corr_matrix = numerical_data.corr()

