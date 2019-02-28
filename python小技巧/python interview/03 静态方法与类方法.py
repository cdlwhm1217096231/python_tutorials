#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 10:48:16
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:
def foo(x):
    print("执行函数foo(%s)" % (x))


class A(object):
    # 对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x)
    def foo(self, x):
        print("执行实例方法: foo(%s, %s)" % (self, x))
    # 类方法一样,只不过它传递的是类而不是实例

    @classmethod
    def class_foo(cls, x):
        print("执行类方法： class_foo(%s, %s)" % (cls, x))
    # 对于静态方法其实和普通的方法一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用a.static_foo(x)或者A.static_foo(x)来调用.

    @staticmethod
    def static_foo(x):
        print("执行静态方法： static_foo(%s)" % (x))


a = A()
# 执行实例方法
a.foo("实例方法")
# 执行类方法
a.class_foo("类方法")
A.class_foo("类方法")
# 静态方法
a.static_foo("静态方法")
A.static_foo("静态方法")
