#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-23 22:49:39
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import threading

# 生成锁对象，全局唯一
lock = threading.Lock()

# 获取锁,没有获得到锁的程序会陷入阻塞，直到程序重新获取到锁才能往下执行
lock.acquire()
# 释放锁，此时，其他程序可以使用锁了
lock.release()


lock = threading.Lock()
with lock:
    # 写自己的业务逻辑代码
    pass

# 死锁
import threading


def main():
    n = 0
    lock = threading.Lock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)


t1 = threading.Thread(target=main)
t1.start()
# 重入锁:解决同一线程中的死锁问题
import threading


def main():
    n = 0
    # 生成可重入锁对象
    lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)


t1 = threading.Thread(target=main)
t1.start()

# 解决多个线程中出现的死锁
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
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


# 使用上面定义的排序方法
import threading
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
"""
多进程是真正的并行，而多线程是伪并行，实际上他只是交替执行，由于GIL导致的。
原因:任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
注意:GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。而Python解释器，并不是只有CPython，除它之外，还有PyPy，Psyco，JPython，IronPython等。在绝大多数情况下，我们通常都认为 Python == CPython，所以也就默许了Python具有GIL锁这个事。
解决方法:1.使用多进程代替多线程。 2.更换Python解释器，不使用CPython
"""
