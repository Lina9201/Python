import json

class Operation_json:
    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open("../dataconfig/GetTest.json") as fp:
            data = json.load(fp)
            return data

    def get_correctdata(self,  id):
        return self.data[id]


if __name__ == '__main__':
    opra = Operation_json()
    #print(opra.get_correctdata('LoginSuccess'))


