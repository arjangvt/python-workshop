# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import numpy as np

# Enable inline plotting

#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#ts = ts.cumsum()
#ts.plot()

#df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
#df = df.cumsum()
#df.plot();

ts = pd.Series(np.random.randn(1000))
df = pd.DataFrame(np.random.randn(1000, 5), index=ts.index, columns=list('ABCDE'))
# Purely integer-location based indexing for selection by position.
df.iloc[5].plot(kind='bar');
plt.axhline(0, color='k')
plt.show()





#Location = r'Data\births1880.csv'
#df = pd.read_csv(Location)
#print(df)

#df = pd.read_csv(Location, header=None)
#print(df)

#df = pd.read_csv(Location, names=['Names','Births'])
#print(df)


# Analazing the data
# Method 1:
#Sorted = df.sort_values(['Births'], ascending=False)
#print(Sorted.head(1))
#print(df['Births'].max())

# Create graph
#df['Births'].plot()

# Maximum value in the data set
#MaxValue = df['Births'].max()

# Name associated with the maximum value
#MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
#Text = str(MaxValue) + " - " + MaxName

# Add text to graph
#plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
#                 xycoords=('axes fraction', 'data'), textcoords='offset points')

#print("The most popular name")
#df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used
#plt.show()

