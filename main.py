
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
from datetime import datetime
#import matplotlib as plt

Forbes_top2000= pd.read_csv("Forbes Top2000 2017.csv")
#print(Forbes_top2000.head())
Forbes_top2000.drop(columns="Unnamed: 0",axis=1,inplace=True)
#print(Forbes_top2000.head())
Forbes_missing=Forbes_top2000.isnull().sum()
#print(Forbes_missing)
Forbes=Forbes_top2000.fillna("unknown")
#print(Forbes.info())
#print(Forbes.head())

Forbes_sectors=Forbes[["Sector","Market Value"]]
#print(Forbes_sectors.head())
Best_sector=Forbes_sectors.groupby("Sector")["Market Value"].sum()
#print(Best_sector)

#Best_sector.plot(kind="bar",title="Top Sectors", rot=340)
#plt.x_label=("Sector")
#plt.y_label=("Market_share,$")
#plt.show()
#plt.savefig("Forbes Top Sectors.png")

Doge=pd.read_csv("Dogecoin Historical Data.csv")
#print(Doge.info())
Doge_2020_2021=Doge.head(481)

#Chart to overview of stock price change
Doge.plot(x="Date", y="Price",rot=90,title='Doge Stock price Apr 2021 - Jun 2017')
plt.show()

#Chart looking at Jan 2020 to Apr 2021.
Doge_2020_2021.plot(x="Date", y="Price",title='Doge stock price Apr 2012 - Jan 2020')

plt.show()
#outlier is date with greates % increase.
Doge_change=Doge.loc[:,"Change %"].max()
print(Doge_change)


Doge_sorted=Doge.sort_values("Change %",ascending=0)
#print(Doge_sorted.head())

#plt.plot(Doge.index,Doge["Price"],color='red',linestyle='--')
#plt.show()

Bit =pd.read_csv("Bitcoin Historical Data.csv")

plt.scatter(x=Bit["Date"],y=Bit["Price"])
#plt.show()

Ggl =pd.read_csv("GOOGL.csv",index_col="Date")
AMD = pd.read_csv("AMD.csv",index_col="Date")
#print(Ggl.head())

Ggl ["Diff$"] = Ggl["Close"]-Ggl["Open"]
Ggl_Sorted= Ggl.sort_values("Diff$", ascending=False)
#print(Ggl_Sorted.info())
#Ggl2016_2018= Ggl_Sorted[2016/01/01:2018/12/31]
#print(Ggl2016_2018.head())


Ggl_vs_AMD=Ggl.merge(AMD,on="Date",how='left',suffixes=('_Ggl','_AMD'))
#print(Ggl_vs_AMD.head())

Ggl_AMD_Compare=Ggl_vs_AMD[["Open_Ggl","Open_AMD"]]
#print(Ggl_AMD_Compare.head())
Ggl_Max=Ggl_AMD_Compare.loc[:,"Open_Ggl"].max()
Ggl_Mean=Ggl_AMD_Compare.loc[:,"Open_Ggl"].mean()
Ggl_Min=Ggl_AMD_Compare.loc[:,"Open_Ggl"].min()
Ggl_Std=Ggl_AMD_Compare.loc[:,"Open_Ggl"].std()
#print(Ggl_Max)
#print(Ggl_Mean)
#print(Ggl_Min)
#print(Ggl_Std)
standard_deviation=Ggl_Mean+Ggl_Std
#print(standard_deviation)

#plt.scatter(x="Date", y="Open_Ggl")
#plt.show()


#ploting Google Vs AMD stock prices
fig,ax=plt.subplots()
ax.plot(Ggl_AMD_Compare.index,Ggl_AMD_Compare["Open_Ggl"],color='red')
ax.set_xlabel('Date')
ax.set_ylabel('Google stock Price',color='red')
ax2=ax.twinx()
ax2.plot(Ggl_AMD_Compare.index,Ggl_AMD_Compare["Open_AMD"],color='blue',)
ax2.set_ylabel('AMD stock price',color='blue')
#plt.show()


