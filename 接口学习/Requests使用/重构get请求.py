import requests
import json

url2 = 'http://httpbin.org/get'

data2 = {
    'key1': 'value1',
    'key2': 'value2'
}

def send_get(url3, data3):
    #res = requests.post(url3, data3)
    #return res.json()
    res = requests.get(url3, data3).json()
    return json.dumps(res, indent=2, sort_keys=True)


print(send_get(url2, data2))
