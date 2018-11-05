#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-19 21:50:16
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
'''python3中的多线程模块:
_thread: 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的
threading:  模块除了包含 _thread 模块中的所有方法外，还提供的其他方法:
threading.currentThread(): 返回当前的线程变量
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程
threading.activeCount(): 返回正在运行的线程数量
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
run(): 用以表示线程活动的方法
start():启动线程活动
join([time]): 等待至线程中止
isAlive(): 返回线程是否活动的
getName(): 返回线程名
setName(): 设置线程名
'''
import threading
import _thread
import time
from threading import Thread
"""Python中使用线程有两种方式：函数或者用类来包装线程对象"""

# 1. 使用函数创建多线程
# 语法形式: threading.Thread( function, args, [kwargs] )
# 参数说明: function: 线程函数 args： 传递给线程函数的参数,必须是个tuple类型。 kwargs： 可选参数

# 自定义线程函数
def print_time(name='python'):
    for i in range(2):
        print('hello %s' % name)
        time.sleep(1)
# 创建线程01，不指定参数
thread_01 = Thread(target=print_time)
# 启动线程01
thread_01.start()
# 创建线程02，指定参数
thread_02 = Thread(target=print_time,args=('C++',))
# 启动线程02
thread_02.start()

# 2. 使用类创建多线程
# 首先类要继承自threading.Thread父类，然后在类中有一个run()方法;


class MyThread(Thread):
    def __init__(self, name='PHP'):
        super().__init__()   # 注意: super().__init__() 一定要写，而且要写在最前面，否则会报错。
        self.name=name

    def run(self):          # 类似于方法1中的自定义线程函数,方法的覆写
        for i in range(2):
            print('hello %s' % self.name)
            time.sleep(1)


if __name__ == '__main__':
    thread_03 = MyThread()   #  创建线程03，不指定参数
    thread_04 = MyThread('Java',)  # 创建线程024，指定参数

    thread_03.start()
    thread_04.start()

# 总结:
"""
threading.Thread()类的属性和方法总结:

t=Thread(target=func)
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
"""