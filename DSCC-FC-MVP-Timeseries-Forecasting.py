# Reference: https://www.kaggle.com/code/prashant111/tutorial-time-series-forecasting-with-prophet

"""This module provides a time-series-forecasting visualization"""

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py
py.init_notebook_mode()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('fivethirtyeight')


file = 'fetched.csv'

df = pd.read_csv(file)

# Preview data
df.head()
df.info()

df['Date'] = pd.DatetimeIndex(df['Date'])
df.dtypes


# Visualize the data
ax = df.set_index('Date').plot(figsize=(12, 8))
ax.set_ylabel('Monthly Number of Open Stock')
ax.set_xlabel('Date')

plt.show()