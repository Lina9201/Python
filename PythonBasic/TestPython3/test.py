# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 21:45
# @Author  : zhuxuefei
zd = {
    'name':'zhuxuefei',
    'age':11
}

def test1(**hp):
    hp['name'] = 'Lina'
    hp['pp'] = 'llo'
    print(hp)

test1(**zd)

print(zd.__dict__)