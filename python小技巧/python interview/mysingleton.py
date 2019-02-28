#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-21 09:21:16
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


class My_Singleton(object):
    def __init__(self):
        pass

    def foo(self):
        print("My name is foo!")


my_singleton = My_Singleton()
