# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 22:03
# @Author  : zhuxuefei

class Student():
    # 通过__init__()将认为必须要绑定的属性填写进去
    # 第一个参数就是self表示创建的实例本身，就把各种属性绑定给self
    def __init__(self, name, score):
        self.name = name
        self.score = score

def print_score(std):
    print('%s: %s' % (std.name, std.score))


print(Student)

# 变量stu就是指向Student的实例
stu = Student('Lina', '98')
print(stu)
print(stu.name)
print(stu.score)
# 给实例变量绑定属性
stu.name = "zhuxuefei"
print(stu.name)

print("=======================")
print_score(stu)



