#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 10:16:57
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""
type是用来判断对象的类型，最大的用途是用来动态创建类，当python扫描到class的语法时，就会调用type函数进行类的创建
"""

# 1.如何使用type创建类-----type需要接收3个参数
"""
a. 类的名称，若不指定，也要传入空字符串：""
b. 父类，注意以tuple的形式传入，若没有父类也要传入空tuple：()，默认继承object
c. 绑定的方法或属性，注意以dict的形式传入
"""
# 定义父类


class BaseClass:
    def talk(self):
        print("I am people")


# 准备一个方法
def say(self):
    print("hello")


# 使用type来创建User类
User = type("User", (BaseClass, ), {"name": "user", "say": say})

# 2.理解元类----类是创建对象的模板，元类是创建类的模板
# 可以使用type来创建一个类，是因为其本身是一个元类，使用元类来创建类
"""
type是Python在背后用来创建所有类的元类，我们熟知的类的始祖 object 也是由type创建的。更有甚者，连type自己也是由type自己创建的
"""
print("type的类型:", type(type))
print("object的类型:", type(object))
print("int的类型:", type(int))
print("string的类型:", type(str))
"""
str：用来创建字符串对象的类。
int：是用来创建整数对象的类。
type：是用来创建类对象的类。
"""
# 或者反过来看
"""
一个实例的类型，是类
一个类的类型，是元类
一个元类的类型，是type
"""
# 实例1


class MetaPerson(type):
    pass


class Person(metaclass=MetaPerson):
    pass


Tom = Person()
print("对象的类型:", type(Tom))
print("类的类型:", type(Tom.__class__))
print("元类的类型:", type(Tom.__class__.__class__))


# 实例2
# 注意要从type继承
class BaseClass(type):
    def __new__(cls, *args, **kwargs):
        print("in BaseClass")
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=BaseClass):
    def __init__(self, name):
        self.name = name


user = User("dana")

# 元类的作用:创建API，一个最典型的应用是 Django ORM。
