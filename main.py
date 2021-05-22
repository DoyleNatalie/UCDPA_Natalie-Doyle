
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#project instructions
# 1) Real World Scenario - Project should use a real world finance dataset and include a reference of their source in the report [1]
# 2) Importing data - Retrieve data from online APIs [1] , Import a CSV file into a Pandas DataFrame. [1]
# 3) Analyzing data - Your project should include sorting, indexing, grouping. [1]
# Replace missing values or dropping duplicates. [1] , Looping, iterrows [1] , Merge dataframes [1]
# 4) Python - Use functions to create reusable code. [1] , Numpy. [1] , Dictionary or Lists. [1]
# 5) Visualize - Generate at least two charts using Matplotlib [2]
# 6) Generate Valuable Insights - 5 insights from the visualization. [3]




# 2 import a CSV file into Pandas DataFrame
import pandas as pd
#import matplotlib as plt
Doge =pd.read_csv("Dogecoin Historical Data.csv")
Bit =pd.read_csv("Bitcoin Historical Data.csv")
Google =pd.read_csv("GOOGL.csv",index_col="Date")
AMD = pd.read_csv("AMD.csv",index_col="Date")

print(Google.head())
print(AMD.head())
#print(Doge.head())
#print(Bit.head())

Google_vs_AMD=Google.merge(AMD,on="Date",how='left',suffixes=('_Google','_AMD'))
print(Google_vs_AMD.head())
print(Google_vs_AMD.info())