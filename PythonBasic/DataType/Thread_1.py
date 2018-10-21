import threading
import time

def chi():
    print("吃火锅开始：")
    time.sleep(1)
    print("吃着火锅：唰羊肉")
    time.sleep(1)
    print("吃着火锅：唰牛肉")
    time.sleep(1)
    print("吃着火锅：唰肉丸")
    time.sleep(1)

def heng():
    print("哼着小曲：")
    time.sleep(1)
    print("哼着小曲1!")
    time.sleep(1)
    print("哼着小曲2！")
    time.sleep(1)
    print("哼着小曲3！")
    time.sleep(1)

# 创建线程数组
threads = []
# 创建线程1，并加入到线程数组
t1 = threading.Thread(target=chi)
threads.append(t1)
# 创建线程2，并加入到线程数组
t2 = threading.Thread(target=heng)
threads.append(t2)

if __name__== "__main__":
    # 启动线程
    for t in threads:
        t.start()
