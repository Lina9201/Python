# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:37
# @Author  : zhuxuefei
import json

def obj_to_json(obj):
    """
    将对象转换成json
    obj.__dict__将对象转换成字典
    json.dumps(dict) 将字典转换成json
    :param obj:
    :return:
    """
    return json.dumps(obj.__dict__)

def json_to_obj(j):
    return json.loads(j).__dict__

