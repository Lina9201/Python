# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 20:30
# @Author  : zhuxuefei

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

stu1 = Student('Lina')
stu2 = Student('Zhu')
stu3 = Student('Zhu2')
print(stu1.count)
print(Student.count)
