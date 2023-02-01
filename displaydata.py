import pandas as pd

class Display:
    """Stock Data Display"""
    pd.set_option("display.max_rows",None)
    df = pd.read_csv("fetched.csv")
    
    print(df)

Display()
