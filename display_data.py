"""This module provides a way to display csv file in tabular format
"""
# import pandas as pd
from prettytable import from_csv

class Display:
    """Display the required data in the desired format"""
    def display_csv(self):
        """Stock Data Display"""
        # pd.set_option("display.max_rows",None)
        # stock_data = pd.read_csv("fetched.csv")
        # print(stock_data)
        with open("fetched.csv",encoding="utf8") as file_pointer:
            mytable = from_csv(file_pointer)
        print(mytable)
