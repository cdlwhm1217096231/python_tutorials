#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 15:31:47
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
线程中通信方法大致有3种:1.threading.Event 2.threading.Condition  3.queue.Queue
"""
# 1.Event事件
"""
Python提供了非常简单的通信机制threading.Event，通用的条件变量。多个线程可以等待某个事件的发生，在事件发生后，所有的线程都会被激活。常用方法:

event = threading.Event()
# 重置event，使得所有该event事件都处于待命状态
event.clear()
# 等待接收event的指令，决定是否阻塞程序执行
event.wait()
# 发送event指令，使所有设置该event事件的线程执行
event.set()
"""
import time
import threading


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print("Thread:{} start at {}".format(
            self.name, time.ctime(time.time())))
        # 等待event.set()后，才能往下执行
        self.event.wait()
        print("Thread:{} finish at {}".format(
            self.name, time.ctime(time.time())))


threads = []
event = threading.Event()
# 定义5个线程
[threads.append(MyThread(str(i), event)) for i in range(1, 6)]
# 重置event,使得event.wait()起到阻塞作用
event.clear()
# 启动所有线程
[t.start() for t in threads]
print("等待5s...")
time.sleep(5)
print('唤醒所有线程...')
event.set()
"""
总结:所有线程都启动t.start()后，并不会执行完。而是都在self.event.wait()停止了，需要通过event.set()来给所有线程发送执行指令才能往下执行
"""


# 2.Condition(与Event类似，没有多大区别)
"""
cond = threading.Condition()

# 类似lock.acquire()
cond.acquire()

# 类似lock.release()
cond.release()

# 等待指定触发，同时会释放对锁的获取,直到被notify才重新占有琐。
cond.wait()

# 发送指定，触发执行
cond.notify()
"""
import time
import threading


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)  # 确保先执行Seeker中的方法
        self.cond.acquire()

        print(self.name + ": 我已经把眼睛蒙上了")
        self.cond.notify()
        self.cond.wait()
        print(self.name + ": 我找到你了哦")
        self.cond.notify()

        self.cond.release()
        print(self.name + ": 我赢了")


class Seeker(threading.Thread):
    def __init__(self, name, cond):
        super(Seeker, self).__init__()
        self.name = name
        self.cond = cond

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ": 我已经藏好了,你快来找我吧")
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print(self.name + ":被你找到了,哎...")


cond = threading.Condition()
seeker = Seeker("seeker", cond)
hider = Hider(cond, "hider")
seeker.start()
hider.start()
# 通过cond来通信，阻塞自己，并使对方执行。从而，达到有顺序的执行。

# 3.Queue队列
"""
从一个线程向另一个线程发送数据最安全的方式可能就是使用queue库中的队列了。创建一个被多个线程共享的Queue 对象，这些线程通过使用put() 和 get() 操作来向队列中添加或者删除元素。

from queue import Queue


# maxsize默认为0，不受限
# 一旦大于0，而消息数又达到限制，q.put()也将阻塞
q = Queue(maxsize=0)

# 阻塞程序，等待队列消息
q.get()

# 获取消息，设置超时时间
q.get(timeout=5.0)

# 发送消息
q.put()

# 等待所有的消息都被消费完
q.join()

# 以下三个方法，知道就好，代码中不要使用

# 查询当前队列的消息个数
q.qsize()

# 队列消息是否都被消费完，True/False
q.empty()

# 检测队列里消息是否已满
q.full()
"""
from queue import Queue
from threading import Thread
import time


class Student(threading.Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            # 阻塞程序，时刻监听老师，接收消息
            msg = self.queue.get()
            # 一旦发现老师点名到自己名字时，赶紧回答到
            if msg == self.name:
                print("{}:到!".format(self.name))
            else:
                print("{}同学没到,等着补考吧!".format(msg))


class Teacher:
    def __init__(self, queue):
        self.queue = queue

    def call(self, student_name):
        print("老师:{}来了没?".format(student_name))
        # 发送消息，要点谁的名
        self.queue.put(student_name)


queue = Queue()
teacher = Teacher(queue=queue)
s1 = Student(name="小明", queue=queue)
s2 = Student(name="大拿", queue=queue)
s1.start()
s2.start()
print("开始点名...")
teacher.call('小明')
time.sleep(1)
teacher.call('大明')
