import pandas as pd
import requests
import json

def getAll():

    # API request receives all information from database
    request = requests.get('http://127.0.0.1:5005/all')
    json_info = json.loads(request.text)
    return pd.DataFrame(json_info)


def getAllFighters():

    # API request receives all fighter names from database
    request = requests.get('http://127.0.0.1:5005/allFighters')
    json_info = json.loads(request.text)
    return pd.DataFrame(json_info)




