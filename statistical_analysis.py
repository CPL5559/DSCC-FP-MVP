import pandas as pd
import numpy as np

class Display:

    """Stock Data Display"""
    pd.set_option("display.max_rows",None)
    df = pd.read_csv("fetched.csv")
    # print(df)

    """display mean of data"""
    x = np.mean(df)
    print(x)

    min_val = min(df)
    max_val = max(df)
    range_data = (min_val, max_val)
    print("range of data:\n", range_data)
   
    """displaying all statistics of data"""
    print(df.describe())

    stats_numeric = df['Open'].describe()
    print("statistics of Open:\n", stats_numeric)

    def stats_display(num):
        data_frame = pd.read_csv("fetched.csv")
        stats_numeric = data_frame[num].describe()
        print("statistics of Open:", stats_numeric)
    stats_display(open)
Display()

class Statistics:

    def min_max_range(self, df):
        min_val = df.min()
        print("min data:\n", min_val)
        max_val = df.max()
        print("max data:\n", max_val)
        range_data = (min_val, max_val)
        print("Range:\n", range_data)
        #return min_val, max_val, range_data

    def central_tendency(self,df):
        mean_data = df.mean()
        median_data = df.median()
        mode_data = df.mode()
        return mean_data, median_data, mode_data
        


df = pd.read_csv("fetched.csv")
stat = Statistics()
print(stat.min_max_range(df))
print(stat.central_tendency(df))