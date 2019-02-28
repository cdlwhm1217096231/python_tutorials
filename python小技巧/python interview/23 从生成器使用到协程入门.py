#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-24 16:13:07
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 1.可迭代、生成器、迭代器
"""
可迭代对象:字符串、list、tuple、dict、deque等
验证是否是可迭代对象、生成器、迭代器的方法，使用isinstance()方法
"""
import collections
from collections.abc import Iterable, Iterator, Generator

# 字符串

ss = "NJUST"
print("字符串:{}".format(ss))
print("是否是可迭代对象:{}".format(isinstance(ss, Iterable)))
print("是否是迭代器:{}".format(isinstance(ss, Iterator)))
print("是否是生成器:{}".format(isinstance(ss, Generator)))
print()

# list

lis = [23, 'haha', "cat", 666]
print("列表:{}".format(lis))
print("是否是可迭代对象:{}".format(isinstance(lis, Iterable)))
print("是否是迭代器:{}".format(isinstance(lis, Iterator)))
print("是否是生成器:{}".format(isinstance(lis, Generator)))
print()

# 字典dict

dic1 = {"Curry": "USA", "Yao": "China", "诺维斯基": "Germany"}
print("字典:{}".format(dic1))
print("是否是可迭代对象:{}".format(isinstance(dic1, Iterable)))
print("是否是迭代器:{}".format(isinstance(dic1, Iterator)))
print("是否是生成器:{}".format(isinstance(dic1, Generator)))
print()
# deque
de = collections.deque("abcdefg")
print("deque:{}".format(de))
print("是否是可迭代对象:{}".format(isinstance(de, Iterable)))
print("是否是迭代器:{}".format(isinstance(de, Iterator)))
print("是否是生成器:{}".format(isinstance(de, Generator)))
print()
# 总结:所有的可迭代对象都不是迭代器和生成器，但都可以用for循环进行遍历;可迭代对象其内部实现了一个__iter__()魔法方法
# 可以通过dir()方法来查看是否有__iter__()来判断一个变量是否是可迭代对象


# 2.迭代器(与可迭代对象相比，内部函数实现仅仅多了一个__next__()函数)
# 可以不使用for循环来获取元素，可以直接使用next()方法来实现
"""
迭代器是在可迭代对象的基础上实现的，要创建一个迭代器，首先必须要有一个可迭代对象，所以下面是介绍如何创建一个可迭代对象，并用创建的可迭代对象创建一个迭代器。
"""


class MyList(object):  # 定义可迭代对象类
    def __init__(self, num):
        self.end = num  # 上界
    # 返回一个实现了__iter__()和__next__()的迭代器类的实例

    def __iter__(self):
        return MyListIterator(self.end)


class MyListIterator(object):  # 定义迭代器类
    def __init__(self, end):
        self.data = end  # 上界
        self.start = 0

    # 返回该对象的迭代器类的实例，因为自己就是迭代器，所以返回self
    def __iter__(self):
        return self
    # 迭代器必须实现的方法

    def __next__(self):
        while self.start < self.data:
            self.start += 1
            return self.start - 1
        raise StopIteration


my_list = MyList(5)  # 得到一个可迭代对象
print(isinstance(my_list, Iterable))
print(isinstance(my_list, Iterator))
# 迭代
for i in my_list:
    print(i)
my_iterator = iter(my_list)  # 得到一个迭代器对象
print("是否是可迭代对象：{}".format(isinstance(my_iterator, Iterable)))
print("是否是迭代器：{}".format(isinstance(my_iterator, Iterator)))
# 迭代
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


astr = "abcd"  # 创建字符串，它可以是可迭代对象
aIterator = iter(astr)  # 通过iter()方法，将可迭代对象转化为迭代器
print(isinstance(aIterator, Iterator))
print(next(aIterator))
print(next(aIterator))
print(next(aIterator))
print(next(aIterator))
# 总结：迭代器其内部实现了__next__()这个魔法函数，可以通过dir()方法来查看变量是否是迭代器


# 3.生成器generator：为了实现一个在计算下一值时不需要浪费空间的结构。生成器是在迭代器的基础上(可以使用for循环和next())再实现了yield,yield相当于函数中的return，在每次next()或者进行for循环时，都会在yield这里将新的值返回回去，并在这里阻塞，等待下一次的调用。实现节省内存，实现异步编程。

# 创建一个生成器有两种方法:改进版的列表生成式和实现yield的函数
# (1).使用改进版的列表生成式，注意不是[],而是()
L = (x**2 for x in range(10))
print("L是一个函数对象:{}".format(L))
print(isinstance(L, Generator))
print("将生成器对象转换成list进行输出:{}".format(list(L)))
# (2).实现yield的函数


def my_generator(n):
    now = 0
    while now < n:
        yield now
        now += 1


gen = my_generator(10)  # 生成器对象
print("生成器对象:%s" % gen)
print(isinstance(gen, Generator))
print(list(gen))

# 总结：可迭代对象和迭代器，是将所有的值都生成后再存放在内存中，而生成器则是把需要的元素临时生成，节省时间与空间。

# 4.运行和激活生成器
# 由于生成器并不是一次生成所有元素,而是一次一次的执行返回,激活生成器执行的两种方法:next()和generator.send(None)


def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1


gen = mygen(4)
# 通过交替执行，来说明这两种方法是等价的
print(gen.send(None))
print(next(gen))
print(gen.send(None))
print(next(gen))

# 5.生成器的执行状态
# 生成器在其生命周期中，会有4个状态：gen_created等待开始执行--->gen_running解释器正在执行(多线程应用中才能看到该状态)--->gen_suspend在yield表达式处暂停--->gen_closed执行结束
from inspect import getgeneratorstate


def gen(n):
    now = 0
    while now < n:
        yield now
        now += 1


gen = gen(2)
print(getgeneratorstate(gen))  # created

print(next(gen))
print(getgeneratorstate(gen))  # suspend

print(next(gen))
gen.close()
print(getgeneratorstate(gen))  # close

# 6.生成器的异常处理
# 在生成器工作过程中，如果生成器不满足生成元素的条件，就会抛出异常StopIteration


def gen1(n):
    now = 0
    while now < n:
        yield now
        now += 1
    raise StopIteration   # 抛出异常


gen = gen1(2)
print(next(gen))
print(next(gen))
# print(next(gen))

# 7.从生成器过渡到协程yield
# 在生成器暂停的时候向其发送一点东西，协程与线程有很多类似点：多个协程之间只会交叉串行执行；不同点：线程之间要频繁进行切换、加锁、解锁，从复杂度和效率上来看，比协程麻烦。协程通过使用yield暂停生成器，可以将程序的执行流程交给其他的子程序，从而实现不同子程序之间的交替执行。


def jump_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index  # yield index是将index返回给外部调用程序；jump = yield可以接收外部程序通过send()发送的信息，并赋值给jump
        if jump is None:
            jump = 1
        index += jump


itr = jump_range(5)
print(next(itr))
print(itr.send(2))
print(next(itr))
print(itr.send(-1))
