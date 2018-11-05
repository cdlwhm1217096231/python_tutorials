#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/20 9:49'
__author__ = 'cdl'

import time
import threading

"""线程中的锁机制"""

"""
有两个线程A和B，A和B里的程序都加了同一个锁对象,当线程A率先执行到lock.acquire()(拿到全局唯一的锁后).
线程B只能等到线程A释放锁lock.release()后（归还锁）才能运行lock.acquire()（拿到全局唯一的锁）并执行后面的代码
"""
# 使用锁
lock = threading.Lock()  # 生成锁对象，全局唯一
lock.acquire()  # 获取锁。未获取到的线程会阻塞程序，直到获取到锁才会往下执行
lock.release()  #  释放锁，归回锁，其他线程可以拿去用了
# 注：lock.acquire() 和 lock.release()必须成对出现。否则就有可能造成死锁

# 为了避免出现死锁情况，推荐使用上下文管理器来加锁
lock = threading.Lock()
with lock:        # with语句会在这个代码块执行前自动获取锁，在执行结束后自动释放锁
    # 这里写自己的代码
    pass
# 使用锁的意义? -----------加锁是为了对锁内资源（变量）进行锁定，避免其他线程篡改已被锁定的资源，以达到我们预期的效果。
# 对比不用锁的线程
# def job1():
#     global n
#     for i in range(10):
#         n += 1
#         print('job1', n)
# def job2():
#     global n
#     for i in range(20):
#         n += 10
#         print('job2', n)
#
# n = 0
# threading_01 = threading.Thread(target=job1)
# threading_02 = threading.Thread(target=job2)
# threading_01.start()
# threading_02.start()
# 加锁之后进行对比
def job1():
    global n, lock
    lock.acquire()  # 获取锁
    for i in range(10):
        n += 1
        print('job1', n)
    lock.release()

def job2():
    global n, lock
    lock.acquire()  # 获取锁
    for i in range(10):
        n += 10
        print('job2', n)
    lock.release()
n = 0
lock = threading.Lock()  # 生成锁对象，全局唯一
threading_01 = threading.Thread(target=job1)
threading_02 = threading.Thread(target=job2)
threading_01.start()
threading_02.start()
# 有时候在同一个线程中，我们可能会多次请求同一资源（就是，获取同一锁钥匙），俗称锁嵌套
def main():
    n = 0
    lock = threading.Lock()
    with lock:
        for i in range(10):
            n += 1
            with lock:  # 第二次获取锁时，发现锁已经被同一线程的人拿走了。自己也就理所当然，拿不到锁，程序就卡住了。
                print(n)

t1 = threading.Thread(target=main)
t1.start()
# 可重入锁RLock，专门来处理这个问题
def num():
    n = 0
    # 生成可重入锁对象
    lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)

t1 = threading.Thread(target=num)
t1.start()
# 防止死锁的加锁机制
"""
出现情况:
同一线程，嵌套获取同把锁，造成死锁
多个线程，不按顺序同时获取多个锁。造成死锁
具体解释:
线程1，嵌套获取A,B两个锁，线程2，嵌套获取B,A两个锁。 
由于两个线程是交替执行的，是有机会遇到线程1获取到锁A，而未获取到锁B，在同一时刻，线程2获取到锁B，而未获取到锁A。
由于锁B已经被线程2获取了，所以线程1就卡在了获取锁B处，由于是嵌套锁，线程1未获取并释放B，是不能释放锁A的。
这是导致线程2也获取不到锁A，也卡住了。两个线程，各执一锁，各不让步，造成死锁。
"""
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


x_lock = threading.Lock()
y_lock = threading.Lock()
def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')
t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()
t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()