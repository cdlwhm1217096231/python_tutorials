#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:41:53
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用
"""
# 装饰器的作用就是为已经存在的对象添加额外的功能。

from functools import wraps
import datetime


def makebold(fn):
    @wraps(fn)
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped   # 最外层函数返回内部函数的函数名


def makeitalic(fn):  # fn = hello
    @wraps(fn)
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


# 调用上述函数
@makebold
@makeitalic
def hello():
    return "hello word"


print(hello())
print('被装饰的函数名：', hello.__name__)
print('---------------------分隔线------------------------')


# 装饰器demo
def decorate(fn):
    @wraps(fn)
    def wrapper():
        return str(fn()) + "。同时，也是我的生日！"
    return wrapper

# 被装饰的函数


@decorate
def log():
    return "今天的日期是:{}".format(datetime.datetime.today())


print(log())
print('被装饰的函数是：', log.__name__)
