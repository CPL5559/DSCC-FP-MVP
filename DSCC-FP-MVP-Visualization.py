"""This module contains the visualization class"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Visualizaton:
    '''This class wraps seaborn functions into simple class methods'''
    def linemap(self,dataframe,col,col1):
        ''' The function makes line plots when we pass dataframe and two labels from dataframe'''
        sns.lineplot(x=dataframe[col], y =dataframe[col1])
        plt.show()

    def boxplot(self,dataframe,col):
        ''' The function makes a boxplot when we pass dataframe and one label from dataframe '''
        sns.set_style('whitegrid')
        sns.boxplot(x=dataframe[col])
        plt.show()

    def heatmap(self,dataframe):
        ''' The function makes a heatmap when we pass dataframe
          to show correlation among all the numerical columns in dataframe'''
        sns.heatmap(dataframe.corr(), annot=True, linewidth=.5)
        plt.show()

df = pd.read_csv("fetched.csv")
visualization = Visualizaton()
visualization.heatmap(df)
