# -*- coding:utf-8 -*-
a = 6
b = 7
c = 8
t = 3
s = []
# 生成的组合
for i in range(t+1):
    s1 = a*i
    s.append(s1)
    for j in range(t+1):
        s2 = a*i+b*j
        s.append(s2)
        for k in range(t+1):
            s3 = a*i + b*j + c*k
            s.append(s3)

