import requests
import json


login_url = 'http://172.50.10.42:8000/v1/tokens'

login_data = {
    "authType": "password",
    "params": {
        "username": "zhuxuefei",
        "password": "Q+1Al2vwhFS9P0qpfg30cQ=="
    }
}


def login(url, data):
    res = requests.post(url, data)
    print(res.json())

login(login_url, login_data)