# Run this app with `python .\DSCC-FC-MVP-InteractiveVisualization.py`
# Reference: https://dash.plotly.com/layout
# visit http://127.0.0.1:8050/ in your web browser.

"""This module contains the interative dashboard visualization class"""
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

app = Dash(__name__)

df = pd.read_csv('fetched.csv')

df['Date'] = pd.to_datetime(df.Date,errors='ignore')
df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
df['Date'] = pd.to_datetime(df.Date,errors='ignore')
# line_plot = px.line(df, x="Date", y=["Open","Close"], render_mode="svg")

line_plot = go.Figure([
    go.Scatter(
        name='Measurement',
        x=df['Date'],
        y=df['Open'],
        mode='lines',
        line=dict(color='rgb(31, 119, 180)'),
    ),
    go.Scatter(
        name='Upper Bound',
        x=df['Date'],
        y=df['High'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=df['Date'],
        y=df['Low'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])
box_plot = px.box(df, x=["Open","Close"], notched=True)

heat_map = px.imshow(round(df.corr(numeric_only=True),3), text_auto=True)

histogram = px.histogram(df, x="Volume")

app.layout = html.Div(children=[
    html.H1(children='DSCC-FC-MVP'),

    html.Div(children='''
        Dash: A web application framework for your financial data (Apple & Samsung).
    '''),

    dcc.Graph(
        id='line-plot',
        figure=line_plot
    ),

    dcc.Graph(
        id='box-plot',
        figure=box_plot
    ),

    dcc.Graph(
        id='heatmap',
        figure=heat_map
    ),

    dcc.Graph(
    id='histogram',
    figure=histogram
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
