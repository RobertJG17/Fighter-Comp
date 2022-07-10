from dash import dcc, html
import dash_bootstrap_components as dbc

def create_card(fighter_href, name):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.Div(
                        [
                            dbc.CardImgOverlay(
                                children=[
                                    html.Img(
                                        src=f"{fighter_href}",
                                        className="fighter-href",
                                        style={
                                            # "opacity": ".4",
                                            "z-index": "1",
                                            "position": "relative",
                                            "padding-bottom":"10px"
                                        }
                                    )
                                ],
                            ),

                            html.H4(
                                name,
                                className="card-title",
                                style=dict(
                                    display="inline-table",
                                    color="black",
                                    font="30px",
                                    zIndex = "1",
                                    position = "relative"
                                )
                            )
                        ],

                        className="title-date",
                    ),

                ]
            )
        ],
        className='fighter-card'
    )
