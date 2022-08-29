from database import DataBase
from flask import Flask
import pandas as pd


# Flask app instantiation
app = Flask(__name__)
db = DataBase()

@app.route('/allFighters')
def get_fighters():
    query = db.queryHandler('fighters')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    return postgres_fighter_table.to_json()

@app.route('/all')
def get_all():
    query = db.queryHandler('all')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    return postgres_fighter_table.to_json()

@app.route('/basicFighterInfo')
def get_info():
    query = db.queryHandler('basic')
    postgres_fighter_table = pd.DataFrame(data=query.fetchall(), columns=query.keys())

    return postgres_fighter_table.to_json()


if __name__ == '__main__':
    app.run('0.0.0.0', 5005)