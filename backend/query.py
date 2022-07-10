from event import DataBase
from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/fighters')
def get_fighters():
    db = DataBase()
    db.get_engine()

    postgres_fighter_table = db.queryHandler('fighters')

    df = pd.DataFrame.from_records(postgres_fighter_table)

    return 'information successfully created as DataFrame'


@app.route('/all')
def get_all():
    db = DataBase()
    db.get_engine()

    postgres_fighter_table = db.queryHandler('all')

    df = pd.DataFrame.from_records(postgres_fighter_table)

    return 'information successfully created as DataFrame'



if __name__ == '__main__':
    app.run('0.0.0.0', 5005)