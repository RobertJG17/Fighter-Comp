from layout import layout
from app import app
import callbacks


app.layout = layout


if __name__ == '__main__':

    app.run_server('0.0.0.0', debug=True)