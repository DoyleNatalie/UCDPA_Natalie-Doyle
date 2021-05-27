

# project instructions
# 1) Real World Scenario - Project should use a real world finance dataset and include a reference of their source
# 2) Importing data - Retrieve data from online APIs [1] ,Looping, iterrows [1]
# 4) Python - Use functions to create reusable code. [1] , Numpy. [1] , Dictionary or Lists. [1]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Forbes_top2000 = pd.read_csv("Forbes Top2000 2017.csv")
#print(Forbes_top2000.head())
Forbes_top2000.drop(columns="Unnamed: 0", axis=1, inplace=True)
#print(Forbes_top2000.head())
Forbes_missing = Forbes_top2000.isnull().sum()
#print(Forbes_missing)
Forbes = Forbes_top2000.fillna("unknown")
#print(Forbes.info())


Forbes_sectors = Forbes[["Sector", "Market Value"]]
#print(Forbes_sectors.head())

# Data grouped by 'sectors' to find their total market share
Best_sector = Forbes_sectors.groupby("Sector")["Market Value"].sum()
#print(Best_sector)

#Best_sector.plot(kind="bar", title="Top Sectors", rot=340)
#plt.x_label = "Sector"
#plt.y_label = "Market_share,$"
#plt.show()
# plt.savefig("Forbes Top Sectors.png")

Doge = pd.read_csv("Dogecoin Historical Data.csv")
#print(Doge.info())

# Chart to overview of stock price change
#Doge.plot(x="Date", y="Price", rot=90, title='Doge Stock price Apr 2021 - Jun 2017')
#plt.show()
#plt.savefig("Doge Stock price Apr 2021 - Jun 2017")

# Subset 2021 - 2020 stock price data
Doge_2020_2021 = Doge.head(481)

# Chart looking at Jan 2020 to Apr 2021.
#Doge_2020_2021.plot(x="Date", y="Price", title='Doge stock price Apr 2012 - Jan 2020', color='red')
#plt.show()
#plt.savefig("Doge stock price Apr 2012 - Jan 2020")

# Sort data by change % to find the outlier, the date with greatest % increase.
#Outlier = Doge.sort_values(["Change %"], ascending=False)
#print(Outlier.head(1))

#Doge_change = Doge.loc[:, "Change %"].max()

#Ggl = pd.read_csv("GOOGL.csv", index_col="Date")
#AMD = pd.read_csv("AMD.csv", index_col="Date")
#print(Ggl.head())

# Merge Google and AMD data.
#Ggl_vs_AMD = Ggl.merge(AMD, on="Date", how='left', suffixes=('_Ggl', '_AMD'))
#print(Ggl_vs_AMD.head())

# Subset for Open stock price for both Data sets.
#Ggl_AMD_Compare = Ggl_vs_AMD[["Close_Ggl", "Close_AMD"]]
#print(Ggl_AMD_Compare.info())

#Ggl_Max = Ggl_AMD_Compare.loc[:, "Close_Ggl"].max()
#Ggl_Mean = Ggl_AMD_Compare.loc[:, "Close_Ggl"].mean()
#Ggl_Min = Ggl_AMD_Compare.loc[:, "Close_Ggl"].min()
#Ggl_Std = Ggl_AMD_Compare.loc[:, "Close_Ggl"].std()
# print(Ggl_Max)
# print(Ggl_Mean)
# print(Ggl_Min)
# print(Ggl_Std)

#standard_deviation = Ggl_Mean+Ggl_Std
#print(standard_deviation)

# plotting Google Vs AMD stock prices
#fig, ax = plt.subplots()
#ax.plot(Ggl_AMD_Compare["Close_Ggl"], color='red')
#ax.set_ylabel("Google stock Price", color='red')
#ax2 = ax.twinx()
#ax2.plot(Ggl_AMD_Compare["Close_AMD"], color='blue',)
#ax2.set_ylabel("AMD stock price", color='blue')
#ax.set_xlabel("Growth by Date (2009 - 2018)")
#ax.legend(["google Stock Price", "AMD Stock Price"])
#ax.set_title("Google Vs AMD stock growth")
#plt.show()
#plt.savefig("Ggl_Vs_AMD chart")

#Glg_AMD_2017_2018 = Ggl_AMD_Compare["2017-01-01":"2018-12-31"]
#print(Glg_AMD_2017_2018.head())



## update to graph both separately
#fig, ax = plt.subplots()
#ax.plot(Glg_AMD_2017_2018["Close_Ggl"], color='red')
#ax.set_ylabel("Google stock 2017 - 2018", color='red')
#ax2 = ax.twinx()
#ax2.plot(Glg_AMD_2017_2018["Close_AMD"], color='blue',)
#ax2.set_ylabel("AMD stock 2017 - 2018", color='blue')
#ax.set_xlabel("Growth by Date (2017 - 2018)")
#ax.legend(["google Stock Price", "AMD Stock Price"])
#ax.set_title("Google Vs AMD growth 2017 - 2018")
#plt.show()

Google = pd.read_csv("GOOGL.csv")
A_M_D = pd.read_csv("AMD.csv")

#Google_2017_2018 = Google["2017-01-01":"2018-12-31"]
#AMD_2017_2018 = A_M_D["2017-01-01":"2018-12-31"]

Google.plot(x="Date", y="Close", rot=90, title='Google 2009- 2018')
plt.x_label = "Date 2009-2018"
plt.y_label = "Market_share,$"


A_M_D.plot(x="Date", y="Close", rot=90, title='AMD 2009 - 2018',color='red')
plt.x_label = "Date 2009-2018"
plt.y_label = "Market_share,$"
#plt.show()

Google_2Years = Google.tail(365)
AMD_2years = A_M_D.tail(365)

print(Google_2Years.head())
print(AMD_2years.head())
Google_2Years.plot(x="Date", y="Close", rot=90, title='Google 2017- 2018')
AMD_2years.plot(x="Date", y="Close", rot=90, title='AMD 2017 - 2018',color='red')
plt.show()

# Dictionaries or list - use Numpy