import requests
import json

class RunMain:
    def __init__(self, url, method, data):
        self.res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)

    def run_main(self, url, method, data):
        self.res = None
        if method == 'Get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    run = RunMain(url,'Get', data)
    print(run.res)
