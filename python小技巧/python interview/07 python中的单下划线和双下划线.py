#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 09:43:25
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


class MyClass(object):
    def __init__(self):
        self.__superprivate = "hello"
        self._semiprivate = ", world!"


mc = MyClass()
# print(mc.__superprivate)
print(mc._semiprivate)
print(mc.__dict__)
print(mc._MyClass__superprivate)


"""
总结:
1.__foo__:一种约定，python内部的名字，用来区别其他用户自定义的命名，以防冲突
例如: __init__(), __del__(), __call__()这些特殊的方法

2._foo:一种约定，用来指定变量私有，程序员用来指定私有变量的一种方式，不能用from module import *导入,其他方面和公有一样访问

3.__foo:解释器用_类名__foo来代替这个名字，以区别和其他类相同的命名，它无法直接像公有成员一样随便访问，
通过  对象名._类名.__xxx  这样的方式访问
"""
