#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-18 08:55:35
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 新式类与经典类

# 1.python3中取消了经典类，默认都是新式类，并且不必显示的继承object
"""
class Person(object):
    pass
class Person():
    pass
class Person:
    pass
三种方法是等价的，并无差别
"""

# 2.python2中，默认都是经典类，只有显示继承了object才是新式类
"""
class Person(object):   # 新式类写法
    pass
class Person():  # 经典类写法
    pass
class Person:  # 经典类写法
    pass

"""

# 3.新式类与经典类的区别
"""
最明显的区别是继承搜索的顺序发生改变：经典类多继承搜索顺序(从左到右深度优先搜索顺序)
新式类多继承搜索顺序(广度优先搜索顺序):先在水平方法查找，然后向上查找
"""
