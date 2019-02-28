#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 10:59:53
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 1.类变量
"""
​是可在类的所有实例之间共享的值（也就是说，它们不是单独分配给每个实例的）。例如下例中，num_of_instance 就是类变量，用于跟踪存在着多少个Test 的实例。
"""
# 实例变量-----实例化之后，每个实例单独拥有的变量


class Test:
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


class Person:
    name = "aaa"


if __name__ == '__main__':
    print(Test.num_of_instance)
    t1 = Test("Jack")
    print(Test.num_of_instance)
    t2 = Test("dana")
    print(Test.num_of_instance)
    print(t1.name, t1.num_of_instance)
    print(t2.name, t2.num_of_instance)
    print("*" * 20)
    p1 = Person()
    p2 = Person()
    p1.name = "bbb"
    print(p1.name)
    print(p2.name)
    print(Person.name)
