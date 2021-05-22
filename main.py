
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#project instructions
# 1) Real World Scenario - Project should use a real world finance dataset and include a reference of their source in the report [1]
# 2) Importing data - Retrieve data from online APIs [1] , Import a CSV file into a Pandas DataFrame. [1]
# 3) Analyzing data - Your project should include sorting, indexing, grouping. [1]
# Replace missing values or dropping duplicates. [1] , Looping, iterrows [1] , Merge dataframes [1]
# 4) Python - Use functions to create reusable code. [1] , Numpy. [1] , Dictionary or Lists. [1]
# 5) Visualize - Generate at least two charts using Matplotlib [2]
# 6) Generate Valuable Insights - 5 insights from the visualization. [3]


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as plt

Forbes_top2000= pd.read_csv("Forbes Top2000 2017.csv")
#print(Forbes_top2000.head())
Forbes_top2000.drop(columns="Unnamed: 0",axis=1,inplace=True)
#print(Forbes_top2000.head())
Forbes_missing=Forbes_top2000.isnull().sum()
#print(Forbes_missing)
Forbes_cleandata=Forbes_top2000.fillna("unknown")
Forbes=Forbes_cleandata.isnull().sum()
#print(Forbes)

Doge =pd.read_csv("Dogecoin Historical Data.csv")
Bit =pd.read_csv("Bitcoin Historical Data.csv")
Doge_sorted =Doge.sort_values("Change %",ascending=False)
#print(Doge_sorted.head())


Ggl =pd.read_csv("GOOGL.csv",index_col="Date")
AMD = pd.read_csv("AMD.csv",index_col="Date")

Ggl_vs_AMD=Ggl.merge(AMD,on="Date",how='left',suffixes=('_Ggl','_AMD'))
#print(Ggl_vs_AMD.head())

Ggl_AMD_Compare=Ggl_vs_AMD[["Open_Ggl","Open_AMD"]]
#print(Ggl_AMD_Compare.head())

#ploting Google Vs AMD stock prices
fig,ax=plt.subplots()
ax.plot(Ggl_AMD_Compare.index,Ggl_AMD_Compare["Open_Ggl"],color='red')
ax.set_xlabel('Date')
ax.set_ylabel('Google stock Price',color='red')
ax2=ax.twinx()
ax2.plot(Ggl_AMD_Compare.index,Ggl_AMD_Compare["Open_AMD"],color='blue',)
ax2.set_ylabel('AMD stock price',color='blue')
plt.show()
