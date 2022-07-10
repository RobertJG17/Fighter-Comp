from layout import layout
from dash import dcc, html
from app import app


app.layout = layout


if __name__ == '__main__':

    app.run_server('0.0.0.0', debug=True)