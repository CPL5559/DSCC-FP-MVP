"""This module provides a time-series-forecasting visualization"""

from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

class ProphetPredict:
    """The class provides method to use Facebook prophet for predictions"""
    def get_predictions(self,dataframe,period_count):
        """The method takes a dataframe with two columns date and values 
        and the number of days to make a prediction and returns plots 
        with predictions, overall trend and weekly seasonality"""
        dataframe.columns = ['ds','y']
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=period_count)
        predictions = model.predict(future)
        print(predictions.tail())

        print(predictions.columns)
        model.plot(predictions)

        model.plot_components(predictions)
        plt.show()

file = 'fetched.csv'
df = pd.read_csv(file)
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
df['Date'] = pd.to_datetime(df.Date,errors='ignore')

# Aggregate to the open data level
open_stock = df
open_stock = df.drop(columns=['High', 'Low', 'Close', 'Adj Close', 'Volume'])
open_stock = open_stock.groupby(['Date','Open'], as_index=False).sum()
print(15 * '==')
print('         Open Data')
print(15 * '==')
print(open_stock)

predict = ProphetPredict()
predict.get_predictions(open_stock,31)
