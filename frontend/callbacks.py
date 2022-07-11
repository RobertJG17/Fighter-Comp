from dash.dependencies import Input, Output
from pyparsing import line
from app import app
from components.card import create_card
from interface import getAllFighters
from dash.exceptions import PreventUpdate
import plotly.express as px


@app.callback(Output('card-stack', 'children'),
              Input('fighter-dropdown', 'value'))
def render_card(value):
    cards = []
    data = getAllFighters()

    if not value:
        raise PreventUpdate

    filtered = data[data['fighter'].isin(value)]

    cards = [
        create_card(
            filtered.iloc[num]['href'], filtered.iloc[num]['fighter'], filtered.iloc[num]['height'], 
            filtered.iloc[num]['age'], filtered.iloc[num]['hometown'], filtered.iloc[num]['style'],
            filtered.iloc[num]['trains-at'], filtered.iloc[num]['weight-class']
        )
        for num in range(len(filtered))
    ]

    return cards


# @app.callback(Output('graph', 'figure'),
#               Input('fighter-dropdown', 'value'))
# def plot_graphs(value):
#     if value is None:
#         raise PreventUpdate

#     data = getAllFighters()
#     theta = ['ss-absorbed-pm', 'ss-attempted', 'ss-def', 'ss-landed', 'ss-landed-pm']
#     r=[data[data.fighter.isin(value)][attr] for attr in theta]

#     print(r)

#     line_graph = px.line_polar(theta=theta, r=r)

#     return line_graph