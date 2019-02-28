#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 11:07:42
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 自省就是面向对象语言所写的程序在运行时,就能知道对象的类型.简单一句就是运行时能够获得对象的类型
# 比如type(),dir(),getattr(),hasattr(),isinstance().

a = [1, 2, 3]
b = {"a": 1, "b": 2, "c": 3}
c = True
print(type(a), type(b), type(c))
print(isinstance(a, list))
