import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# API
ISS_persons = requests.get("http://api.open-notify.org/astros.json")
Space_people = ISS_persons.json()
print(Space_people['number'])

for Name in Space_people['people']:
    print(Name['name'])

# importing CSV file dropping and replacing missing values.
Forbes_top2000 = pd.read_csv("Forbes Top2000 2017.csv")
print(Forbes_top2000.head())
Forbes_top2000.drop(columns="Unnamed: 0", axis=1, inplace=True)
print(Forbes_top2000.head())
Forbes_missing = Forbes_top2000.isnull().sum()
print(Forbes_missing)
Forbes = Forbes_top2000.fillna("unknown")
print(Forbes.info())
Forbes_sectors = Forbes[["Sector", "Market Value"]]
print(Forbes_sectors.head())

# Data grouped by 'Sectors' to find their total market share
Best_sector = Forbes_sectors.groupby("Sector")["Market Value"].sum()
print(Best_sector)

Best_sector.plot(kind="bar", title="Top Sectors", rot=340)
plt.x_label = "Sector"
plt.y_label = "Market_share,$"
plt.show()
# plt.savefig("Forbes Top Sectors.png")

Doge = pd.read_csv("Dogecoin Historical Data.csv")
print(Doge.info())

# Chart to overview of stock price change
Doge.plot(x="Date", y="Price", rot=90, title='Doge Stock price Apr 2021 - Jun 2017')
plt.show()
# plt.savefig("Doge Stock price Apr 2021 - Jun 2017.png")

# Subset 2021_2020 stock price data
Doge_2020_2021 = Doge.head(481)

# Chart looking at Jan 2020 to Apr 2021.
Doge_2020_2021.plot(x="Date", y="Price", title='Doge stock price Apr 2021 - Jan 2020', color='red')
plt.show()
# plt.savefig("Doge stock price Apr 2021 - Jan 2020.png")

# Sorting data by change % to find the outlier, the date with greatest % increase.
Outlier = Doge.sort_values(["Change %"], ascending=False)
print(Outlier.head(1))

Average_price = Doge.loc[:, "Change %"].mean()
print(Average_price)

Above_Avg = Doge[Doge["Change %"] > 5.045144]
print(Above_Avg.count())

Above_Standard = Doge.loc[:, "Change %"].std()
print(Above_Standard)

# Find days which had a change % greater than the standard deviation between 2020 and 2021 year to date.
Extraordinary_days = Doge[Doge["Change %"] > 164.647]
print(Extraordinary_days)

# Import CSV indexing with the Date column.
Ggl = pd.read_csv("GOOGL.csv", index_col="Date")
AMD = pd.read_csv("AMD.csv", index_col="Date")

# Merge Google and AMD data.
Ggl_vs_AMD = Ggl.merge(AMD, on="Date", how='left', suffixes=('_Ggl', '_AMD'))
print(Ggl_vs_AMD.head())

# Subset for Open stock price for both Data sets.
Ggl_AMD_Compare = Ggl_vs_AMD[["Close_Ggl", "Close_AMD"]]

# plotting Google Vs AMD stock prices 2009 - 2018
fig, ax = plt.subplots()
ax.plot(Ggl_AMD_Compare["Close_Ggl"], color='red')
ax.set_ylabel("Google stock Price", color='red')
ax2 = ax.twinx()
ax2.plot(Ggl_AMD_Compare["Close_AMD"], color='blue',)
ax2.set_ylabel("AMD stock price", color='blue')
ax.set_xlabel("Growth by Date (2009 - 2018)")
ax.legend(["google Stock Price", "AMD Stock Price"])
ax.set_title("Google Vs AMD stock growth")
plt.show()
# plt.savefig("Ggl_Vs_AMD chart.png")

# Subset data to review only data form 2017 - 2018 for both companies.
Glg_AMD_2017_2018 = Ggl_AMD_Compare["2017-01-01":"2018-12-31"]

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
plt.show()
# plt.savefig("Ggl_Vs_AMD 2017 - 2018 chart.png")

# using Numpy arrays to review if sales targets are reached
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
Sales_yr1 = [215.11, 548.36, 156.89, 468.25, 216.94, 258.36, 227.48, 164.12, 756.21, 564.12, 658.12, 389.16]
Sales_array = np.array(Sales_yr1)
Targets = [200, 200, 300, 300, 300, 400, 400, 400, 500, 500, 500, 500]
Targets_array = np.array(Targets)

indexing_Qtr1 = np.array([0, 1, 2])
indexing_Qtr2 = np.array([3, 4, 5])
indexing_Qtr3 = np.array([6, 7, 8])
indexing_Qtr4 = np.array([9, 10, 11])
Qtr1_sales = Sales_array[indexing_Qtr1].sum()
Qtr2_sales = Sales_array[indexing_Qtr2].sum()
Qtr3_sales = Sales_array[indexing_Qtr3].sum()
Qtr4_sales = Sales_array[indexing_Qtr4].sum()
Qtr1_Targets = Targets_array[indexing_Qtr1].sum()
Qtr2_Targets = Targets_array[indexing_Qtr2].sum()
Qtr3_Targets = Targets_array[indexing_Qtr3].sum()
Qtr4_Targets = Targets_array[indexing_Qtr4].sum()

# Review if targets are being achieved.
Qtr1_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr2_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr3_target_complete = Qtr1_sales >= Qtr1_Targets
Qtr4_target_complete = Qtr1_sales >= Qtr1_Targets

print(Qtr1_target_complete)
print(Qtr2_target_complete)
print(Qtr3_target_complete)
print(Qtr4_target_complete)

Sales_Yr2 = [301.25, 256.48, 320.36, 556.25, 425.48, 236.48, 268.49, 584.36, 843.16, 677.68, 799.26, 862.46]
Targets_Yr2 = [400, 400, 400, 400, 400, 300, 300, 600, 600, 600, 700, 700]
Sales_Yr2_array = np.array(Sales_Yr2)
Target_Yr2_array = np.array(Targets_Yr2)

plt.plot(Months, Sales_yr1, color='blue', label='Sales Yr1')
plt.plot(Months, Sales_Yr2, color='green', label='Sales Yr2')
plt.plot(Months, Targets, color='red', linestyle='--', label='Targets')
plt.xlabel('Months')
plt.ylabel('Sales per Month $')
plt.title('Yr1 & Yr2 Sales Vs Target year 1')
plt.legend()
plt.show()
# plt.savefig("Sales Vs Yr1 Targets chart.png")

plt.bar(Months, Sales_yr1, color='blue', label='Sales Yr1')
plt.plot(Months, Targets, color='red', linestyle='--', label='Targets_Yr2')
plt.xlabel('Months')
plt.ylabel('Sales per Month $')
plt.title('Sales Yr1 vs Targets')
plt.legend()
plt.show()
# plt.savefig("Sales Yr1 vs Targets chart.png")

plt.bar(Months, Sales_Yr2, color='green', label='Sales Yr2')
plt.plot(Months, Targets_Yr2, color='red', linestyle='--', label='Targets_Yr2')
plt.xlabel('Months')
plt.ylabel('Sales per Month $')
plt.title('Yr2 Sales Vs Yr2 Target')
plt.legend()
plt.show()
# plt.savefig("Yr2 Sales Vs Yr2 Target chart.png")
