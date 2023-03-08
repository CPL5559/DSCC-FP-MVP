"""This module provides a time-series visualization"""

import pandas as pd 
import numpy as np 
from pandas import DataFrame
from  matplotlib import pyplot 
from datetime import datetime       # To access datetime 
from pandas import Series  
import statsmodels.api as sm
#from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose        # To work on series 
#%matplotlib inline 
import warnings                     # To ignore the warnings
warnings.filterwarnings("ignore")

class Timeseriesanalysis:
    '''
        We are using follwoing time series analysis modules - 
        1.ETS Models & Decomposition - Error Trend Seasonality
        2. EWMA Models - Exponentially Weighted Moving Averages
        3. ARIMA Models - Automative Regression Integration Moving Average
    '''
    def etsmodels(self,dataframe,col):
        '''
        ETS(Error Trend Seasonality) models take each of the terms (Error-Trend-Seasonality) for smoothing 
        purposes - and may add them, multiply them, or leave some of them out of the model.
        '''
        dataframe.rolling(7).mean()
        seasonal_result= seasonal_decompose(df[col], model='additive', period=12)
        seasonal_result.plot()
        pyplot.show()

    def ewmamodels(self,dataframe,col):
        '''
            Exponentially Weighted Moving Averages solve some of these issues, in particular:
            EWMA allows you to reduce the lag time from SMA and puts more weight on values that occur more recently
            The amount of weight applied to the recent values depends on the parameters used in the EWMA and the number 
            of periods in the window size
        '''
        # create EWMA
        df['EWMA-30'] = df[col].ewm(span=30).mean()
        #create a new dataframe EWMA of the label that we want to perform ewm model
        df['EWMA'] = df[col]
        # plot EWMA
        df[['EWMA', 'EWMA-30']].plot(figsize=(10,8))
        pyplot.show()

    def arimamodels(self,dataframe,col):
        '''
            Time Series Model - AR: Autoregression. A model uses the dependent relationship between an observation and some number of lagged observations.
            I: Integrated. The use of differencing of raw observations (e.g. subtracting an observation from an observation at the previous time step) in order to make the time series stationary.
            MA: Moving Average. A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.
        '''
        model = sm.tsa.arima.ARIMA(df[col], order=(5,1,0)) #5 for autoregressison, difference order = 1, moving average model = 0 
        model_fit = model.fit()
        # summary of fit model
        print(model_fit.summary())
        # line plot of residuals
        residuals = DataFrame(model_fit.resid)
        residuals.plot()
        pyplot.show()
        # density plot of residuals
        residuals.plot(kind='kde') # no bias found in the data.
        pyplot.show()
        # summary stats of residuals
        print(residuals.describe())

df = pd.read_csv('fetched.csv')
timeseriesanalysis = Timeseriesanalysis()
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df.set_index('Date',inplace = True)
timeseriesanalysis.arimamodels(df,'Open')
