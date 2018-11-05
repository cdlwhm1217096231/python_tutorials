#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/24 10:33'
__author__ = 'cdl'

"""元类"""
# 类是如何产生的----------真正的创建是由type来创建的
# 如何使用type创建类
"""
首先，type()需要接收三个参数:
        1. 类的名称，若不指定，也要传入空字符串：""
        2. 父类，注意以tuple的形式传入，若没有父类也要传入空tuple:()，默认继承object
        3. 绑定的方法或属性，注意以dict的形式传入
"""
# 准备一个基类（父类）
class BaseClass:
    def talk(self):
        print("i am people")
# 准备一个方法
def say(self):
    print("hello")
# 使用type来创建User类
User = type("User", (BaseClass, ), {"name":"user", "say":say})

# 理解什么是元类-----------类就是用来创建对象的「模板」, 元类就是创建类的「模板」。
print(type(type))  # type：是用来创建类对象的类。
print(type(object))
print(type(int))  # int：是用来创建整数对象的类。
"""
一个实例的类型，是类
一个类的类型，是元类
一个元类的类型，是type
"""
class MetaPerson(type):
    pass


class Person(metaclass=MetaPerson):
    pass

Tom = Person()
print(type(Tom))
print(type(Tom.__class__))
print(type(Tom.__class__.__class__))
# 完整版
# 注意要从type继承
class BaseClass(type):
    def __new__(cls, *args, **kwargs):
        print("in BaseClass")
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=BaseClass):
    def __init__(self, name):
        self.name = name

user = User("wangbm")
# 元类的作用就是创建API，一个最典型的应用是 Django ORM。
