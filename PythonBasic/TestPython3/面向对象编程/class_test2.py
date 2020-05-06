# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 19:18
# @Author  : zhuxuefei

class Student():
    def __init__(self,name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == "Male":
            print("是男性")
        elif gender == "Female":
            print("是女性")

stu1 = Student("zhuxuefei", "Female")
print(stu1.get_gender())
stu1.set_gender("Male")
