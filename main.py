

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
plt.x_label = "Sector"
plt.y_label = "Market_share,$"
#plt.show()
#plt.savefig("Forbes Top Sectors.png")

Doge = pd.read_csv("Dogecoin Historical Data.csv")
#print(Doge.info())

# Chart to overview of stock price change
Doge.plot(x="Date", y="Price", rot=90, title='Doge Stock price Apr 2021 - Jun 2017')
#plt.show()
#plt.savefig("Doge Stock price Apr 2021 - Jun 2017")

# Subset 2021_2020 stock price data
Doge_2020_2021 = Doge.head(481)

# Chart looking at Jan 2020 to Apr 2021.
Doge_2020_2021.plot(x="Date", y="Price", title='Doge stock price Apr 2012 - Jan 2020', color='red')
#plt.show()
#plt.savefig("Doge stock price Apr 2012 - Jan 2020")

# Sort data by change % to find the outlier, the date with greatest % increase.
Outlier = Doge.sort_values(["Change %"], ascending=False)
#print(Outlier.head(1))

# Confirm outlier value.
Doge_greatest_change = Doge.loc[:, "Change %"].max()
#print(Doge_greatest_change)

Average_price = Doge.loc[:, "Change %"].mean()
#print(Average_price)

Above_Avg = Doge[Doge["Change %"] > 5.045144]
#print(Above_Avg.count())

Above_Standard = Doge.loc[:, "Change %"].std()
#print(Above_Standard)

Extraordinary_days = Doge[Doge["Change %"] > 164.647]
#print(Extraordinary_days)

Ggl = pd.read_csv("GOOGL.csv", index_col="Date")
AMD = pd.read_csv("AMD.csv", index_col="Date")
#print(Ggl.head())

# Merge Google and AMD data.
Ggl_vs_AMD = Ggl.merge(AMD, on="Date", how='left', suffixes=('_Ggl', '_AMD'))
#print(Ggl_vs_AMD.head())

# Subset for Open stock price for both Data sets.
Ggl_AMD_Compare = Ggl_vs_AMD[["Close_Ggl", "Close_AMD"]]
#print(Ggl_AMD_Compare.info())


# plotting Google Vs AMD stock prices
fig, ax = plt.subplots()
ax.plot(Ggl_AMD_Compare["Close_Ggl"], color='red')
ax.set_ylabel("Google stock Price", color='red')
ax2 = ax.twinx()
ax2.plot(Ggl_AMD_Compare["Close_AMD"], color='blue',)
ax2.set_ylabel("AMD stock price", color='blue')
ax.set_xlabel("Growth by Date (2009 - 2018)")
ax.legend(["google Stock Price", "AMD Stock Price"])
ax.set_title("Google Vs AMD stock growth")
#plt.show()
#plt.savefig("Ggl_Vs_AMD chart")

Glg_AMD_2017_2018 = Ggl_AMD_Compare["2017-01-01":"2018-12-31"]
#print(Glg_AMD_2017_2018.head())



# Graph Google and AMD 2017 - 2018 to review growth in last year
fig, ax = plt.subplots()
ax.plot(Glg_AMD_2017_2018["Close_Ggl"], color='red')
ax.set_ylabel("Google stock 2017 - 2018", color='red')
ax2 = ax.twinx()
ax2.plot(Glg_AMD_2017_2018["Close_AMD"], color='blue',)
ax2.set_ylabel("AMD stock 2017 - 2018", color='blue')
ax.set_xlabel("Growth by Date (2017 - 2018)")
ax.legend(["google Stock Price", "AMD Stock Price"])
ax.set_title("Google Vs AMD growth 2017 - 2018")
#plt.show()

Google = pd.read_csv("GOOGL.csv")
A_M_D = pd.read_csv("AMD.csv")

#Google_2017_2018 = Google["2017-01-01":"2018-12-31"]
#AMD_2017_2018 = A_M_D["2017-01-01":"2018-12-31"]

Google.plot(x="Date", y="Close", rot=90, title='Google 2009- 2018')
#plt.x_label = "Date 2009-2018"
#plt.y_label = "Market_share,$"

A_M_D.plot(x="Date", y="Close", rot=90, title='AMD 2009 - 2018',color='red')
plt.x_label = "Date 2009-2018"
plt.y_label = "Market_share,$"
#plt.show()

Google_2Years = Google.tail(365)
AMD_2years = A_M_D.tail(365)

#print(Google_2Years.head())
#print(AMD_2years.head())

Google_2Years.plot(x="Date", y="Close", rot=90, title='Google 2017- 2018')
AMD_2years.plot(x="Date", y="Close", rot=90, title='AMD 2017 - 2018',color='red')
#plt.show()

# Dictionaries or list - use Numpy

Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
Sales = [215.11, 548.36, 156.89, 468.25, 216.94, 258.36, 327.48, 164.12, 756.21, 564.12, 658.12, 389.16]
Annual_sales_array = np.array ([Months, Sales])
Sales_array = np.array(Sales)
Targets = [300, 300, 300, 300,300, 300, 400, 400, 400, 400, 400, 200]
Targets_array = np.array(Targets)

indexing_Qtr1 = np.array([0,1,2])
indexing_Qtr2 = np.array([3,4,5])
indexing_Qtr3 = np.array([6,7,8])
indexing_Qtr4 = np.array([9,10,11])

Qtr1_sales = Sales_array[indexing_Qtr1].sum()
Qtr2_sales = Sales_array[indexing_Qtr2].sum()
Qtr3_sales = Sales_array[indexing_Qtr3].sum()
Qtr4_sales = Sales_array[indexing_Qtr4].sum()
Qtr1_Targets = Targets_array[indexing_Qtr1].sum()
Qtr2_Targets = Targets_array[indexing_Qtr2].sum()
Qtr3_Targets = Targets_array[indexing_Qtr3].sum()
Qtr4_Targets = Targets_array[indexing_Qtr4].sum()

Qtr1_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr2_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr3_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr4_target_complete = Qtr1_sales >= Qtr1_Targets

print(Qtr1_target_complete)
print(Qtr2_target_complete)
print(Qtr3_target_complete)
print(Qtr4_target_complete)