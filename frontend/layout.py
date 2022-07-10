from dash import dcc, html
import interface

layout = html.Div([
    dcc.Dropdown(
        options=[
            {'label': fighter, 'value': fighter} 
            for fighter in interface.getAllFighters().fighter.values
        ],
        id='fighter-dropdown'
    ),

    html.Div(
        id='card-stack', 
        style={'display':'grid'}
    )
])