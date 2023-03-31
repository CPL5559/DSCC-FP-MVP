# Run this app with `python .\DSCC-FC-MVP-InteractiveVisualization.py`
# Reference: https://dash.plotly.com/layout
# visit http://127.0.0.1:8050/ in your web browser.

"""This module contains the interative dashboard visualization class"""
# %matplotlib inline
from io import BytesIO
import base64
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from data_collection import DataCollection
from DSCC_FP_MVP_Timeseries_Forecasting import ProphetPredict

app = Dash(__name__)

app.layout = html.Div(id='main-div', style = {'text-align':'center'}, children=[
    html.H1(children='DSCC-FC-MVP'),

    html.H3(children='Financial data dashboard.'),

    html.Div(style = {'display':'inline-flex'}, children=[dcc.Dropdown(
        options = [
                    {'label':'Apple', 'value':'AAPL'},
                    {'label':'Samsung','value':'SMSN.IL'}
                ],
        value = 'AAPL',
        id='dropdown',
        style = {'width':'150px'}
    )]),

    html.H3(children='The stock prices for Calendar year 2021 along with intraday maximum and minimum'),
    dcc.Graph(id='line-plot'),
    
    html.H3(children='Major statistical characteristics for Open and Close prices'),
    dcc.Graph(id='box-plot'),

    html.H3(children='Heat map displaying the corelation between different prices and volume'),
    dcc.Graph(id='heatmap'),

    html.H3(children='A view of distribution of the volume amount'),
    dcc.Graph(id='histogram'),

    html.H3(children='Drag the slider below to change number of days!'),

    html.Div(style={'width':'700px','margin-left':'500px'}, children = [dcc.Slider(0, 365, 1, value=180, marks=None,
    tooltip={"placement": "bottom", "always_visible": True}, id='day_slider')]),

    html.H3(id='slider-string',style={'text-align':'center'}),

    html.Div(children = [html.Img(id = 'prediction_plot', src = '',style={'width':'800px'}),

    html.Img(id = 'component_plot', src = '')], style={'display':'inline-flex'})
])

@app.callback(
    Output('line-plot', 'figure'),
    Output('box-plot', 'figure'),
    Output('heatmap', 'figure'),
    Output('histogram', 'figure'),
    Output(component_id='prediction_plot', component_property='src'),
    Output(component_id='component_plot', component_property='src'),
    Output(component_id='slider-string', component_property='children'),
    Input('dropdown', 'value'),
    Input('day_slider','value')
)
def update_output(dropdown_value,slider_value):
    collector = DataCollection()
    data = collector.fetch(dropdown_value)
    collector.save(data)

    df = pd.read_csv('fetched.csv')

    df['Date'] = pd.to_datetime(df.Date,errors='ignore')
    df['Date'] = df['Date'].apply(lambda x : x.strftime('%Y-%m-%d'))
    df['Date'] = pd.to_datetime(df.Date,errors='ignore')
# line_plot = px.line(df, x="Date", y=["Open","Close"], render_mode="svg")

    line_plot = go.Figure([
        go.Scatter(
            name='Open Price',
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

    forecasting = ProphetPredict()
    open_stock = df[['Date','Open']]
    open_stock = open_stock.groupby(['Date','Open'], as_index=False).sum()
    result = forecasting.get_predictions(open_stock,slider_value)
    predictions = result[0]
    model = result[1]

    out_url = fig_to_uri(model.plot(predictions))

    components_url = fig_to_uri(model.plot_components(predictions))

    slider_string = f'Price prediction for {slider_value} days'

    return line_plot, box_plot, heat_map, histogram, out_url, components_url, slider_string

def fig_to_uri(in_fig, close_all=False, **save_args):
    """Save a figure as a URI"""
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return f"data:image/png;base64,{encoded}"

if __name__ == '__main__':
    app.run_server(debug=True)
