import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pandas as pd
import plotly.graph_objects as go 
import dash
from dash import html, dcc

data = pd.read_csv('gapminder_full.csv')
# print(data.head())

new_data = data[data['country'] == 'India']


app = dash.Dash(__name__)
 

app.layout = html.Div([

    html.Div(children=[
        html.H1(children = "Different Graph in this Deshboard", style={'color' : 'aqua', 'text-align' : 'center', 'margin' : '2px'})
    ], style={'border' : '3px black solid', 'float' : 'left', 'width' : '100%', 'height' : '50px'}), 
    

    html.Div(children=[
        dcc.Graph(id='Scatter-plot', 
                  figure={'data' : [go.Scatter(x = data['population'], y = data['gdp_cap'], mode = 'markers')], 'layout' : go.Layout(title='Analysis of Population vs GDP per Capita')})
    ], style={'border' : '3px black solid', 'float' : 'left', 'width' : '49.68%', 'height' : '350px'}), 
    
    
    html.Div(children=[
        dcc.Graph(id='line-plot', figure={'data' : [go.Line(x = new_data['year'], y = new_data['population'])], 'layout' : go.Layout(title='Line Plot')})
    ], style={'border' : '3px black solid', 'float' : 'left', 'width' : '49.68%', 'height' : '350px'})

])

if __name__ == '__main__':
    app.run(debug = True)