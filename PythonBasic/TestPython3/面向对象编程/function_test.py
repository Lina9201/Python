# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 18:52
# @Author  : zhuxuefei

class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

lisa = student('Lisa', 99)
print(lisa.name, lisa.get_grade())
lisa.age = 8
print(lisa.age)
