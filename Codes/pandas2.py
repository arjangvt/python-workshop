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

#ts = pd.Series(np.random.randn(1000))
#df = pd.DataFrame(np.random.randn(1000, 5), index=ts.index, columns=list('ABCDE'))
# Purely integer-location based indexing for selection by position.
#df.iloc[5].plot(kind='bar');
#plt.axhline(0, color='k')
#plt.show()



#df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
#df.plot.box()
#plt.show()

#df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
#color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
#df.plot.box(color=color, sym='r+')
#plt.show()

#df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.area();
#plt.show()

#df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.area(stacked=False);
#plt.show()

#df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.scatter(x='a', y='b');
#plt.show()

#df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
#df.plot.scatter(x='a', y='b', c='c', s=50);
#plt.show()

#series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
#series.plot.pie(figsize=(6, 6))
#plt.show()