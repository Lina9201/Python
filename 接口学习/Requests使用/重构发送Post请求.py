import requests
import json

url2 = 'http://httpbin.org/post'

data2 = {
    'key1': 'value1',
    'key2': 'value2'
}

def send_post(url3, data3):
    #res = requests.post(url3, data3)
    #return res.json()
    res = requests.post(url3, data3).json()
    return json.dumps(res)


print(send_post(url2, data2))
