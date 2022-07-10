import requests
import pandas as pd


def getAllFighters():
    request = requests.get('http://127.0.0.1:5005/all')
    data = pd.DataFrame(request.json()).transpose()
    return data