from dash import dcc, html
import dash_bootstrap_components as dbc
from interface import getAllFighters
import plotly.express as px

layout = html.Div([
    html.H1('Fighter Comparison'),
    dcc.Dropdown(
        options=[
            {'label': fighter, 'value': fighter} 
            for fighter in getAllFighters().fighter.values
        ],

        multi=True,
        id='fighter-dropdown',
        className='dropdown',
        style={'color':'white'}
    ),

    html.Div(
        id='card-stack',
        className='card-stack' 
    )

    # ss-absorbed-pm | ss-attempted | ss-def | ss-landed | ss-landed-pm | 
])
