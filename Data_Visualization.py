# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:46:30 2020

@author: nnath
"""

#DATA VISUALIZATION FOR DATAT SCIENCE
'''
Popular plotting libaries 

MATPLOTLIB : to create 2D graphs ; uses numpy internally
                
PANDAS VISUALISATION : built on Matplotlib
SEABORN : High level interface for attractive and informative statistical graphs
GGPLOT : based on R; Grammer Of Graphics
PLOTLY : Create interactive plots

'''

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'D:\GITHUB\PANDAS\Pandas')
os.listdir()
df_cars = pd.read_csv('CARS.csv',sep=",")

df_cars.isnull().sum()
df_cars.dropna(axis=0,inplace=True)

df_cars.info()

#SCATTER PLOT : or Correlation Plot - used to convery relation between 2 numerical variables

plt.scatter(df_cars['EngineSize'],df_cars['Weight'],c='red')
plt.title('Scatter plot for EngineSize vs Weight')
plt.xlabel('EngineSize')
plt.ylabel('Weight')
plt.show()

#Histogram : used to represent frequency distribution of numerical variables
#height represent the frequency of each range or bin
plt.hist(df_cars['Weight'].head(100))

plt.hist(df_cars['Length'],color='green',edgecolor='white',bins=5)
plt.title('Histogram plot for length of cars')
plt.xlabel('m')
plt.ylabel('Length')

#----------------------------------
'''
# Generate data on commute times.
'''
#1
size, scale = 1000, 10
commutes = np.random.gamma(scale, size=size) ** 1.5
plt.hist(commutes)

#2
size, scale = 1000, 10
commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Counts')
plt.ylabel('Commute Time')
plt.grid(axis='y', alpha=0.75)
#-----------------------------------------

#BAR PLOT : distribution of categorial variables
df = pd.crosstab(index=df_cars['Make'],columns='count',dropna=True)#returns only count column need 'Make' column

df_cars['count']=1
df_cars.groupby(['Make']).count()['count']
df_cars.drop(columns = ['count'], inplace = True)
#df of car name and its count to represent in bar graph
counts = df_cars['Make'].value_counts()#series returned
car_brands = pd.unique(df_cars['Make'])#array returned
index = np.arange(len(car_brands))
plt.bar(index , counts , color = 'red')
plt.bar(index , counts , color = ['red','blue'])
plt.bar(index , counts , color = ['red','blue','yellow','green'])
plt.title('Bar plot for cars')
plt.xlabel('Car brand')
plt.ylabel('Frequency')
plt.xticks(index,car_brands)
'''
dd_sorted = (df_cars['Make'].head(50)).sort_values(ascending=True)
counts = dd_sorted.value_counts().sort_index(ascending=True)#series returned; sort by index 
'''
#counts = df_cars['Make'].head(50).value_counts()
#counts is in descending order and car_brand in random order 
#in plt.bar() we give array to match with the corresponding count and car_brand
counts = df_cars['Make'].head(50).value_counts().sort_index(ascending=True)
car_brands = pd.unique(df_cars['Make'].head(50))#array returned
counts.sort_values()
index = np.arange(len(car_brands))
#plt.bar(index , counts , color = 'red')
#plt.bar(index , counts , color = ['red','blue'])
plt.bar(index , counts , color = ['red','blue','yellow','green'])
plt.title('Bar plot for cars')
plt.xlabel('Car brand')
plt.ylabel('Frequency')
plt.xticks(index,car_brands)#,rotation=70)
