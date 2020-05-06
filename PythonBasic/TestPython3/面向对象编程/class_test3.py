# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 19:43
# @Author  : zhuxuefei
class Animal():
    def run(self):
        print("Animal is running~~~")

class Dog(Animal):
    pass
    # def run(self):
    #     print("Dog is running~~~")

dog = Dog()
dog.run()
# 若实例数据类型是某个子类，那它的数据类型可被看做是父类，但是反过来不行
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
A = Animal()
print(isinstance(A, Dog))

print(dir('ABC'))