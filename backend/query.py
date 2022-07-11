from turtle import pos

from requests import post
from event import DataBase
from flask import Flask
import pandas as pd
import json

app = Flask(__name__)


@app.route('/allFighters')
def get_fighters():
    db = DataBase()
    db.get_engine()

    query = db.queryHandler('fighters')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    return postgres_fighter_table.to_json()


@app.route('/all')
def get_all():
    db = DataBase()
    db.get_engine()

    query = db.queryHandler('all')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    postgres_fighter_table = postgres_fighter_table[(postgres_fighter_table['href'] in (None, '', ' '))]

    return postgres_fighter_table.to_json()



if __name__ == '__main__':
    app.run('0.0.0.0', 5005)