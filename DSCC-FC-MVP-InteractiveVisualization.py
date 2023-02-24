# Run this app with `python .\DSCC-FC-MVP-InteractiveVisualization.py`
# Reference: https://dash.plotly.com/layout
# visit http://127.0.0.1:8050/ in your web browser.

"""This module contains the interative dashboard visualization class"""
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objs as go
from data_collection import DataCollection

app = Dash(__name__)

app.layout = html.Div(id='main-div',children=[
    html.H1(children='DSCC-FC-MVP'),

    html.Div(children='Dash: A web application framework for your financial data.'),

    dcc.Dropdown(
        options = [
                    {'label':'Apple', 'value':'AAPL'},
                    {'label':'Samsung','value':'SMSN.IL'}
                ],
        value = 'AAPL',
        id='dropdown'
    ),

    dcc.Graph(id='line-plot'),

    dcc.Graph(id='box-plot'),

    dcc.Graph(id='heatmap'),

    dcc.Graph(id='histogram')
])

@app.callback(
    Output('line-plot', 'figure'),
    Output('box-plot', 'figure'),
    Output('heatmap', 'figure'),
    Output('histogram', 'figure'),
    Input('dropdown', 'value')
)
def update_output(value):
    collector = DataCollection()
    data = collector.fetch(value)
    collector.save(data)

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

    # fig1 = dcc.Graph(id='line-plot',figure=line_plot)
    # fig2 = dcc.Graph(id='box-plot',figure=box_plot)

    return line_plot, box_plot, heat_map, histogram

if __name__ == '__main__':
    app.run_server(debug=True)
