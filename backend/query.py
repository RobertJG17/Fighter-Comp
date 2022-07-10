from event import DataBase
from flask import Flask
import pandas as pd
import json

app = Flask(__name__)


@app.route('/fighters')
def get_fighters():
    db = DataBase()
    db.get_engine()

    postgres_fighter_table = pd.DataFrame(db.queryHandler('fighters'))

    print(postgres_fighter_table)

    return 'done'


@app.route('/all')
def get_all():
    db = DataBase()
    db.get_engine()

    query = db.queryHandler('all')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    return postgres_fighter_table.transpose().to_json()



if __name__ == '__main__':
    app.run('0.0.0.0', 5005)