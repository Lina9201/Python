import requests
import json

url = 'http://www.imooc.com/passport/user/login'

data = {
    'username':'18994205919',
    'password':'Jz8tfU+e4jh5GjzchJzSI4iY2XCRLvpLCz8CVC5Nl77HfFtVdU2IVZtwmeSfKobettdU/CMdnpB7RiaxSCRBqfFxEqYHTDHtVkvYM9Vf0UBEcoYOh1YmU6tJYhjqzihb1hLnP/56t18uviWJTOqFdBbh0clPdqe2qCmFu8S9yCs='
}


def send_post(url, data):
    res = requests.post(url=url, data=data)
    return res.json()

print(send_post(url, data))
