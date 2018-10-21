# -*- coding:utf-8 -*-

x = [1, 2, 3]
# iter返回一个迭代器对象
its = x.__iter__()
# next方法不断地迭代获取容器中的元素
print(its.__next__())
print(its.__next__())
print(its.__next__())

# for单层循环
for i in range(5):
    print(i)


