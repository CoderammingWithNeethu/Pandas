# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:34:41 2020

@author: nnath
"""

import pandas as pd


tb_A = {'Day':[1,2,3,4,5,6],'Visitors':[100,102,1003,300,400,100],'Bounce_Rate':[20,10,30,20,14,34]}
df_A = pd.DataFrame(tb_A)
print(df_A)

#OPERATIONS

#Slicing

df_A.head(2)#first 2 rows
df_A.tail(2)#last 2 rows

#Merging
#merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
tb_B1 = {'Day':[11,21,31,41,51,61],'Visitors':[1100,1102,11003,1300,1400,1100],'Bounce_Rate':[120,110,130,120,114,134]}

df_B1 = pd.DataFrame(tb_B1,index=[10,11,13,14,15,16])#all columns as common
df_B2= pd.DataFrame( {'Day':[11,21,31,41,51,61],'Visitors':[1100,1102,11003,1300,1400,1100],'Bounce_Rate':[120,110,130,120,114,134]},index=[17,18,19,20,21,22])
merge = pd.merge(df_B1,df_B2)
print(merge)

merge1 = pd.merge(df_B1,df_B2,on='Day')#merge over specific column, keep other columns separate
print(merge1)

#Joining - joining happens on index values

tb_C1 = {'Day':[11,21,31,41,51,61],'Visitors':[1100,1102,11003,1300,1400,1100],'Bounce_Rate':[120,110,130,120,114,134]}

df_C1 = pd.DataFrame(tb_C1,index=[10,21,31,41,15,16])#all columns as common
df_C2= pd.DataFrame( {'Colm1':[11,21,31,41,51,61],'Colum2':[1100,1102,11003,1300,1400,1100]},index=[10,18,19,20,21,23])
join1 = df_C1.join(df_C2)
print(join1)
join2 = df_C2.join(df_C1)
print(join2)

'''
tb_C1 = {'Day':[11,21,31,41,51,61],'Visitors':[1100,1102,11003,1300,1400,1100],'Bounce_Rate':[120,110,130,120,114,134]}

df_C1 = pd.DataFrame(tb_C1,index=[10,21,31,41,15,16])#all columns as common
df_C2= pd.DataFrame( {'Day':[11,21,31,41,51,61],'Visitors':[1100,1102,11003,1300,1400,1100],'Bounce_Rate':[120,110,130,120,114,134]},index=[17,18,19,20,21,22])

join1 = df_C1.join(df_C2)
#ValueError: columns overlap but no suffix specified
error message translates to: 
     "I can see the same column in both tables but you haven't told me to rename either before bringing one of them in"

You either want to delete one of the columns before bringing it in from the other on using del df['column name'], 
or use lsuffix to re-write the original column, or rsuffix to rename the one that is being brought it.
Solution: lsuffix, rsuffix
df_a.join(df_b, on='mukey', how='left', lsuffix='_left', rsuffix='_right')
'''

#Changing Index And Column Headers
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')#graph style

tb_D = {'Day':[1,2,3,4,5,6],'Visitors':[100,102,1003,300,400,100],'BOUNCE_Rate':[20,10,30,20,14,34]}
df_D = pd.DataFrame(tb_D)
print(df_D)
df_D.set_index('Day',inplace = True)
print(df_D)

df_D.plot()#graph
plt.show()

df_D = df_D.rename(columns={'Visitors':'Users'})
print(df_D)


#Concatenation 

concat = pd.concat([df_B1,df_B2])
print(concat)

#Data Munging - data conversion

country = pd.read_csv(r'D:\GITHUB\PANDAS\Pandas\country_code.csv',index_col=0)#no index
country.to_html('D:\GITHUB\PANDAS\Pandas\country_code.html')

