# -*- coding:utf-8 -*-
import math
import random
import cmath
__author__ = u'Lina'


if __name__ == "__main__":
    x = -100
    y = 1.9

    print(u"常用数学函数")
    #  返回绝对值
    print(abs(x))
    #  返回最小值
    print(min(x, int(y)))
    #  返回最大值
    print(max(x, y))
    #  返回平方值
    print(pow(y, 2))
    #  返回平方根
    print(math.sqrt(y))

    print(u"常用随机函数")
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    #  从列表中随机选择一个
    print(random.choice(a))
    #  从指定范围2-100中按5递增的数据集中随机选中一个
    print(random.randrange(2, 100, 5))
    #   生成一个随机数在0-1之间
    print(random.random())

    print(u'常用三角函数')
    x = 100
    print(cmath.cos(x))

    print(u'数字常量')
    #  返回pai值3.14xxx
    print(cmath.pi)

