#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 10:02:33
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# 将列表生成式中的[]改为()后，数据结构将会改变，从列表变为生成器
L = [x * x for x in range(10)]
print("L is a list：{}".format(L))
g = (x * x for x in range(10))
print("g is a generator:{}".format(g))
print("通过list函数将生成器对象转化为列表list:{}".format(list(g)))
"""
生成器的意义:
通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator
"""
