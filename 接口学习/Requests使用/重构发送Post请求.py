import requests
import json

header = {

}

url2 = 'http://httpbin.org/post'

data2 = {
    'key1': 'value1',
    'key2': 'value2'
}
print(type(data2))

def send_post(url3, data3):
    res = requests.post(url3, data3)
    print(res.json())

send_post(url2, data2)
