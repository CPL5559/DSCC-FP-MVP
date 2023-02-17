"""This is the main module of this application"""

import importlib
import pandas as pd
from data_collection import DataCollection
from display_data import Display
Visualization = importlib.import_module('./DSCC-FP-MVP-Visualization.py')
def main():
    """This is the driver function"""

    while True:
        print("-"*25 + "Stock data viewer" + "-"*25)
        print("1. View stock data")
        print("2. Exit")
        option = int(input("Enter option: "))

        if option == 1:
            view_stock_data()

        if option == 2:
            break
    return True

def view_stock_data():
    """This function"""
    print("-"*25 + "Stock data viewer" + "-"*25)
    print("1. View Apple stock data")
    print("2. View Samsung stock data")
    print("3. Exit")

    collector = DataCollection()
    printer = Display()
    option = int(input("Enter option: "))
    if option == 1:
        data = collector.fetch("AAPL")
        view_graphs()
    if option == 2:
        data = collector.fetch("SMSN.IL")
        view_graphs()
    if option == 3:
        return

    collector.save(data)
    printer.display_csv()

def view_graphs():
    """This function"""
    print("-"*25 + "Stock data viewer" + "-"*25)
    print("1. Linegraph")
    print("2. Bar graph")
    print("3. Correlation")
    visualization = Visualization.Visualization()

    option = int(input("Enter option: "))
    dataframe = pd.read_csv("fetched.csv")
    if option == 1:
        dataframe['Date'] = dataframe['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
        visualization.heatmap(dataframe)

    if option == 2:
        visualization.boxplot(dataframe,'Open')

    if option == 3:
        visualization.heatmap(dataframe)
    
if __name__=="__main__":
    main()
