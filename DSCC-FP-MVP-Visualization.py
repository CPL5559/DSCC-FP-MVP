# Importing all the necessary libraries
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
import seaborn as sns
import matplotlib.pyplot as plt

class MVP_Visualizaton:
    '''This class will helps, interact with, and better understand data. Whether simple or complex, the right visualization'''
    def linemap(self,df,col,col1):
        ''' The function is used to plot the line map when we pass dataframe and two labels from dataframe '''
        sns.lineplot(x=df[col], y =df[col1])
        plt.show()

    def boxplot(self,df,col):
        ''' The function is used to plot the box when we pass dataframe and one label from dataframe '''
        sns.set_style('whitegrid')
        sns.boxplot(x=df[col])
        plt.show()

    def heatmap(self,df):
        ''' The function is used to plot the heatmap when we pass dataframe to show correlation among the labels in dataframe '''
        # df = df.drop(columns =['Date'])
        sns.heatmap(df.corr(), annot=True, linewidth=.5)
        plt.show()

df = pd.read_csv("fetched.csv")
visualization = MVP_Visualizaton()
visualization.heatmap(df)