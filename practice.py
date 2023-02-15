import pandas as pd 
import datetime
import warnings
warnings.filterwarnings("ignore")
import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fetched.csv")
col = list(df.columns.values)

df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
df['Date'] = pd.to_datetime(df.Date,errors='ignore')

#df.groupby(df.Date.dt.weekofyear)
#df.groupby(df['Date'].map(lambda x: x.year))
df['Date'] = pd.to_datetime(df['Date']) - pd.to_timedelta(7, unit='d')

#calculate sum of values, grouped by week
df.groupby([pd.Grouper(key='Date', freq='W')])


'''for i in df['Open']:
    sns.set_style('whitegrid')
    sns.boxplot(x=df["Open"])
    '''