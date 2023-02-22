# Run this app with `python .\DSCC-FC-MVP-InteractiveVisualization.py`
# Reference: https://dash.plotly.com/layout
# visit http://127.0.0.1:8050/ in your web browser.

"""This module contains the interative dashboard visualization class"""
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

from dash import Dash, html
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('fetched.csv')

fig = px.scatter(df, x="Close", y="Open",
                 size="Volume", color="High", hover_name="Date",
                 log_x=True, size_max=60)

app.layout = html.Div(children=[
    html.H1(children='DSCC-FC-MVP'),

    html.Div(children='''
        Dash: A web application framework for your financial data (Apple & Samsung).
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
