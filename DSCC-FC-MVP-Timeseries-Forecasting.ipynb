# References: https://www.kaggle.com/code/prashant111/tutorial-time-series-forecasting-with-prophet
#             https://www.phdata.io/blog/facebook-prophet-tutorial-time-series-forecasting/

"""This module provides a time-series-forecasting visualization"""

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py
py.init_notebook_mode()


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


file = 'fetched.csv'
df = pd.read_csv(file)
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
# print(df)


# Preview data
#df.head()
#df.info()
#df.dtypes
print(f'The minimum date is: ', min(df['Date'])) # Minimum date
print(f'The maximum date is: ', max(df['Date'])) # Maximum date

# Aggregate to the open data level
open_stock = df
open_stock = df.drop(columns=['High', 'Low', 'Close', 'Adj Close', 'Volume'])
open_stock = open_stock.groupby(['Date','Open'], as_index=False).sum()
print(15 * '==')
print('         Open Data')
print(15 * '==')
print(open_stock)

# Split into train / test  (Aggregate open level)
train = open_stock[open_stock['Date'] < '2021-01-04']
test = open_stock[open_stock['Date'] >= '2021-12-29']

# Model for open data
# Ref: https://www.phdata.io/blog/facebook-prophet-tutorial-time-series-forecasting/


# Visualize the data
ax = df.set_index('Date').plot(figsize=(12, 8))
ax.set_ylabel('Monthly Number of Stock Data')
ax.set_xlabel('Year - Month')

plt.show()