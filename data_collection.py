"""This module provides functionality to fetch stock data of a desired organization
and save it in a csv file"""
import pandas as pd
import yfinance as yf
import requests_cache
class DataCollection:
    """The class fetches stock data using yfinance library and saves it in csv locally"""
    def save(self,data):
        ''' The funciton is used for the coversion of DataFrame into csv file \n
        It stores the data in the system'''
        #Changing the data into Panda DataFrame
        stock_data = pd.DataFrame(data)
        # Conversion of Pandas into csv file
        stock_data.to_csv('fetched.csv', header = True)
    #using yfinace API
    def fetch(self,name):
        ''' Fetches the data from yfinance with ticker name \n
        Display all the data provided by the tickername '''
    # Ticker Module
        session = requests_cache.CachedSession('yfinance.cache')
        session.headers['User-agent'] = 'my-program/1.0'
        ticker = yf.Ticker(name, session = session)
    # The scraped response will be stored in the cache
        ticker.actions
        data = yf.download(name, start="2021-01-01", end="2021-12-30")
    # Display of Data
        return data[:]
