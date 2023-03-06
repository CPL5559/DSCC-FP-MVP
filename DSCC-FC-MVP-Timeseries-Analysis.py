"""This module provides a time-series visualization"""

import pandas as pd 
import numpy as np                  # For mathematical calculations 
import matplotlib.pyplot as plt     # For plotting graphs 
from datetime import datetime       # To access datetime 
from pandas import Series           # To work on series 
#%matplotlib inline 
import warnings                     # To ignore the warnings
warnings.filterwarnings("ignore")

class Timeseries:
    """Display the required time-series analysis"""
    def timeseries_analysis(self):
        """Time-series visualization"""
        # Apply logic here

df = pd.read_csv("fetched.csv")
ts = Timeseries()