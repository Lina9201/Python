# -*- coding:utf-8 -*-
__author__ = u'Lina'

if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa k a ka,yo yo yo!"
    # 从左往右查找yo
    print(u'从左往右查找yo')
    print(source_str.find('yo'))
    # find若无找到则返回-1,index若未找到则抛出异常
    print(source_str.find('tt'))
    print(source_str.index('yo'))

    #  从右往左查找yo
    print(u'从右往左查找yo')
    print(source_str.rfind('yo'))
    print(source_str.rindex('yo'))

    #  替换所有的yo
    des_str = source_str.replace('yo', 'ha')
    print(des_str)

    #  替换两次yo
    des_str = source_str.replace('yo', 'ha', 2)
    print(des_str)
