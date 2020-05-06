# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 9:41
# @Author  : zhuxuefei
import json
if __name__ == "__main__":
    test1 = {
        'id': 4,
        'name':'vmware'
    }

    test2 = {
        'id': 4,
        'name': 'vmware',
        'code':2000
    }
    for i, j in test1.items():
        if i in test2.keys():
            print(j)
            print(test2[i])
            assert j == test2[i]

    test3 = {
        'id': 5,
        'name':'vmwaretest'
    }
    print(test3.items())
    print(type(test1))
    print(test1)
    print(type(test1))
    test4 =  '{"name":"裸金属资源池","ip":"172.23.1.2"}'
    print(test4)
    print(type(test4))
    print("================")
    print(eval(test4))
    print(type(eval(test4)))
