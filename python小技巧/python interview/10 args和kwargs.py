#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 19:26:46
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 当不确定函数中要传递多少参数时，可以使用*args，它可以传递任意数量的参数


def print_everything(*args):
    for count, thing in enumerate(args):
        print("{0}--->{1}".format(count, thing))


# **kwargs允许你使用没有事先定义的参数名
def table_thing(**kwargs):
    for name, value in kwargs.items():
        print("{0}--->{1}".format(name, value))


# 可以混着使用，命名参数首先获得参数值，然后所有的其他参数都传递给*args和**kwargs
# 命名参数在列表的最前面，如:def table_things(titlestring, **kwargs)
# *args和**kwargs可以同时在函数的定义中，但是*args必须在**kwargs前
def print_three_things(a, b, c):
    print("a ={0}, b={1}, c={2}".format(a, b, c))


if __name__ == '__main__':
    print_everything('banana', 'apple', 'grape')
    table_thing(apple="fruit", bmw='car')
    myList = ['haha', 'dana', 555]
    print_three_things(*myList)
