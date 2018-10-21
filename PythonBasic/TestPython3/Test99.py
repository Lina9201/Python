# -*- coding:utf-8 -*-
# 两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
if __name__ == '__main__':
    # 使用File的open方法打开text1
    fp = open('text1.txt')
    # read读取
    text1 = fp.read()
    # close关闭
    fp.close()
    print(text1)

    fp2 = open('text2.txt')
    text2 = fp2.read()
    # close关闭
    fp2.close()
    print(text2)

    # list(seq)：将元组转换为列表 
    s = list(text1+text2)
    print(s)
    # sort函数进行排序
    s.sort()
    # join函数连接字符串数组，将字符串、元组、列表中的元素以指定的字符连接成一个新的字符串
    s1 = "".join(s)

    fp3 = open("text.txt", "w+")
    fp3.writelines(s1)
    fp3.close()

    fp3 = open("text.txt")
    text = fp3.read()
    fp3.close()
    print(text)







