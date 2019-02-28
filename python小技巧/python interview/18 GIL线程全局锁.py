#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 09:45:56
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
线程全局解释器锁(Global Interpreter Lock),即Python为了保证线程安全而采取的独立线程运行的限制,说白了就是一个核只能在同一时间运行一个线程.对于io密集型任务，python的多线程起到作用，但对于cpu密集型任务，python的多线程几乎占不到任何优势，还有可能因为争夺资源而变慢。
解决办法：多进程或协程(协程也只是单CPU,但是能减小切换代价提升性能).
"""
# 单线程VS多线程VS多进程
"""
开始对比之前，首先定义四种类型的场景： CPU计算密集型、磁盘IO密集型、 网络IO密集型、模拟IO密集型
"""


# CPU计算密集型
def count(x=1, y=1):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


#  磁盘读写IO密集型
def io_disk():
    with open("file.txt", 'w') as f:
        for x in range(500000):
            f.write("python_learning\n")


# 网络IO密集型
import requests
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
url = "https://www.tieba.com/"


def io_web():
    try:
        response = requests.get(url, header=header)
        html = response.text
    except Exception as e:
        return {"error": e}


import time
# 模拟IO密集型


def io_simulation():
    time.sleep(2)


# 比较的指标是：时间，时间花费越少，说明效率越高
from functools import wraps


def timer(model):
    def wrapper(func):
        def decorator(*args, **kwargs):
            type = kwargs.setdefault('type', None)
            t1 = time.time()
            func(*args, **kwargs)  # 被装饰函数
            t2 = time.time()
            cost_time = t2 - t1
            print("{}-{}花费时间:{}s".format(model, type, cost_time))
        return decorator
    return wrapper

# 单线程
# 被装饰函数


@timer("单线程")
def single_thread(func, type=""):
    for i in range(10):
        func()



# 单线程
single_thread(count, type="CPU计算密集型")
single_thread(io_disk, type="磁盘IO密集型")
single_thread(io_web, type="网络IO密集型")
single_thread(io_simulation, type="模拟IO密集型")


# 多线程
# 被装饰函数
from threading import Thread


@timer("多线程")
def multi_thread(func, type=''):
    thread_list = []
    for i in range(10):
        t = Thread(target=func, args=())
        thread_list.append(t)
        t.start()
    e = len(thread_list)
    while True:
        for thred in thread_list:
            if not thred.is_alive():
                e -= 1
        if e <= 0:
            break


# 多线程
multi_thread(count, type="CPU计算密集型")
multi_thread(io_disk, type="磁盘IO密集型")
multi_thread(io_web, type="网络IO密集型")
multi_thread(io_simulation, type="模拟IO密集型")


# 多进程
# 被修饰函数
from multiprocessing import Process


@timer("多线程")
def multi_process(func, type=""):
    process_list = []
    for x in range(10):
        p = Process(target=func, args=())
        process_list.append(p)
        p.start()
    e = process_list.__len__()

    while True:
        for pr in process_list:
            if not pr.is_alive():
                e -= 1
        if e <= 0:
            break


# 多进程
multi_process(count, type="CPU计算密集型")
multi_process(io_disk, type="磁盘IO密集型")
multi_process(io_web, type="网络IO密集型")
multi_process(io_simulation, type="模拟IO密集型")
