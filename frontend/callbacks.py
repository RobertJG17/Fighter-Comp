from dash.dependencies import Input, Output
from app import app
from main import data
from components.card import create_card


@app.callback(Output('card-stack', 'children'),
              Input('fighter-dropdown', 'value'))
def render_card(value):
    cards = []

    for row_num in range(len(data)):
        entry = data.iloc[row_num]

        if entry['fighter'] == value:
            cards.append(create_card(entry['href'], entry['fighter']))

    return cards