import requests


url = 'http://172.20.12.45:8080/operation/active/login'

data = {
    "username": "admin1",
    "password": "21232f297a57a5a743894a0e4a801fc3"
}

header={
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}

res = requests.post(url=url, data=data)

#print(type(res))
#print(res.text)
print(res.json())
#print(res)

for i in range(1, 3):
    print(i)
