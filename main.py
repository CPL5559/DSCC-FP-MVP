"""This is the main module of this application"""

from data_collection import DataCollection
from display_data import Display
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
    if option == 2:
        data = collector.fetch("SMSN.IL")
    if option == 3:
        return

    collector.save(data)
    printer.display_csv()

if __name__=="__main__":
    main()
