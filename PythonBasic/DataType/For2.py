# -*- coding:utf-8 -*-

# for嵌套循环
list1 = ['1', '2', '3', ['a', 'b', 'c']]
for i in list1:
    for j in i:
        print(j)

num = [];
for i in range(2, 100):
    j = 2
    for j in range(2, i):
        if( i % j == 0):
            break
    else:
         num.append(i)
print(num)





