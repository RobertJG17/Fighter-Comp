from dash import dcc, html
import dash_bootstrap_components as dbc

def create_card(fighter_href, name, height, age, hometown, style, trains_at, weight_class):
    return dbc.Card([
            dbc.CardImgOverlay(
                children=[
                    html.Img(
                        src=f"{fighter_href}",
                        className="fighter-href",
                    )
                ],
            ),

            dbc.CardHeader(children=[name], className='card-header'),
            dbc.CardBody([
                html.H6('Weight Class: {}'.format(weight_class)),
                html.Hr(),
                html.H6('Hometown: {}'.format(hometown)),
                html.Hr(),
                html.H6('Trains At: {}'.format(trains_at)),
                html.Hr(),
                html.H6('Style: {}'.format(style)),
                html.Hr(),
                html.H6('Height: {}'.format(height)),
                html.Hr(),
                html.H6('Age: {}'.format(age))
            ], className="card-body")
        ],

        className='card'
    )
