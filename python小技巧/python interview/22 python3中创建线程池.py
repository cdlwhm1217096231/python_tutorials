#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 15:12:49
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 1.使用第三方模块
"""
在使用多线程处理任务时也不是线程越多越好，由于在切换线程的时候，需要切换上下文环境，依然会造成cpu的大量开销。为解决这个问题，线程池的概念被提出来了。预先创建好一个较为优化数量的线程，让过来的任务立刻能够使用，就形成了线程池。
在Python3中，创建线程池是通过concurrent.futures函数库中的ThreadPoolExecutor类来实现的。
"""
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def target():
    for i in range(5):
        print("running thread-{}:{}".format(threading.get_ident(), i))
        time.sleep(1)


# 生成线程池的最大线程为5个
pool = ThreadPoolExecutor(5)
for i in range(100):
    pool.submit(target)   # 往线程中提交并运行

# 2.自定义线程池(使用消息队列来自定义线程池)
import time
import threading
from queue import Queue


def target(q):
    while True:
        msg = q.get()
        for i in range(5):
            print("running thread-{}:{}".format(threading.get_ident(), i))
            time.sleep(1)


def pool(workers, queue):
    for n in range(workers):
        t = threading.Thread(target=target, args=(queue,))
        t.daemon = True
        t.start()


queue = Queue()
# 创建一个线程池，并设置线程数为5
pool(5, queue)
for i in range(100):
    queue.put("start")
# 消息都被消费后才能结束
queue.join()
