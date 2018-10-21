import requests
import json

url = 'http://httpbin.org/post'

data = {
    'key1': 'value1',
    'key2': 'value2'
}

res = requests.post(url=url, data=data)

print(type(res))
print(res.text)
print(res.json())
