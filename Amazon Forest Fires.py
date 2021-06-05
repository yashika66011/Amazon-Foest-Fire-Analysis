# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:22:40 2021

@author: pande
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults() 

#Reading the data
data = pd.read_csv('C:\\amazon\\amazon.csv', thousands = '.')

#Viewing the data
data.shape

data.head()

data.describe(include= "all")
print(data.describe(include= "all"))




#Checking for any missing values
data.isna().sum()
print(data.isna().sum())


#Breaking the dataset into smaller subsets
data = data.replace(0, np.nan)    #convert the 0s to NaN  
print(data)

data2 = data.dropna(subset=['number'])    #drop rows with NaN in the specific column number
print(data2)

data2.describe(include= "all")
print(data2.describe(include= "all"))


#Creating subset of data by grouping the data by month and summing the number
forest_fire_per_month = data2.groupby('month')['number'].sum()
print(forest_fire_per_month)


months_unique = list(data.month.unique()) 
forest_fire_per_month = forest_fire_per_month.reindex(months_unique, axis=0)  #using reindex property to group data monthly, not alphabetically
print(forest_fire_per_month)


#convert the series into a dataframe
forest_fire_per_month = forest_fire_per_month.to_frame()
print(forest_fire_per_month)

forest_fire_per_month.head()
print(forest_fire_per_month.head())


#To set a default index
forest_fire_per_month.reset_index(level=0, inplace=True)
forest_fire_per_month.head()
print(forest_fire_per_month.head())


print(forest_fire_per_month)

plt.figure(figsize=(25, 15)) #specify width and height 
#plt.bar(x-values, y-values) 
plt.bar(
forest_fire_per_month['month'],
forest_fire_per_month['number'], 
color = ("blue")) 

#use .suptitle for the actual title and .title for the subheading
plt.suptitle('Amazon Forest Fires Over the Months', fontsize=20) 
plt.title('Using Data from Years 1998 - 2017', fontsize=20) 
plt.xlabel('Month', fontsize=20) 
plt.ylabel('Number of Forest Fires', fontsize=20)

#plt.text(x-coordinate, y-coordinate, valueOfText, alignmnet)
#this adds text at the top of each bar indicating its value
for i, num in enumerate(forest_fire_per_month['number']):
    plt.text(
        i,
        num + 10000,
        num,
        ha='center',
        fontsize=15)   


#plt.setp is to set a property on an artist object.
#plt.gca() gets the current axes (gca) instance on the current figure #matching the given keyword args.
#xticklabels and yticklabels are nothing but the values of the #lables on the x and y axis.
#The code below lets us set the fontsize and alignment of the x and #y axis tick labels
plt.setp(plt.gca().get_xticklabels(),
         rotation=45,
         horizontalalignment='right',
         fontsize=20)
plt.setp(plt.gca().get_yticklabels(), fontsize=20)









