"""This module contains the statistics class"""
import pandas as pd
class Statistics:
    """This class provides methods to calculate common statistics of the specified dataframe"""
    def minimum(self, dataframe):
        """The function wraps the pandas.DataFrame.min function in a simple class method"""
        return dataframe.min()

    def maximum(self, dataframe):
        """The function wraps the pandas.DataFrame.max function in a simple class method"""
        return dataframe.max()

    def range(self, dataframe):
        """This function return the range of numeric columns in the specified dataframe"""
        return dataframe.max(numeric_only=True) - dataframe.min(numeric_only=True)

    def central_tendency(self, dataframe):
        """This method calculates the mean, median and mode
        of the numeric columns of the dataframe"""
        mean = dataframe.mean(numeric_only=True)
        median = dataframe.median(numeric_only=True)
        return mean, median

df = pd.read_csv("fetched.csv")
stat = Statistics()
print(stat.minimum(df))
print(stat.maximum(df))
print(stat.range(df))
print(stat.central_tendency(df))
