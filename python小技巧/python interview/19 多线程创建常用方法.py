#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 22:27:22
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import time
from threading import Thread


# 自定义线程函数
def my_threadfunc(name='python3'):
    for i in range(2):
        print("hello", name)
        time.sleep(1)


# 创建线程01，不指定参数
thread_01 = Thread(target=my_threadfunc)
# 启动线程01
thread_01.start()


# 创建线程02,指定参数，注意逗号不要少，否则不是一个tuple
thread_02 = Thread(target=my_threadfunc, args=('Curry',))
# 启动线程02
thread_02.start()


import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name='Python3'):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(2):
            print("Hello", self.name)
            time.sleep(1)


# 创建线程03，不指定参数
thread_03 = MyThread()
# 创建线程04，指定参数
thread_04 = MyThread("Curry")
thread_03.start()
thread_04.start()


t = Thread(target=func)

# 启动子线程
t.start()

# 阻塞子线程，待子线程结束后，再往下执行
t.join()

# 判断线程是否在执行状态，在执行返回True，否则返回False
t.is_alive()
t.isAlive()

# 设置线程是否随主线程退出而退出，默认为False
t.daemon = True
t.daemon = False

# 设置线程名
t.name = "My-Thread"
