#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 09:54:40
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# .format在许多方面看起来更便利.对于%最烦人的是它无法同时传递一个变量和元组
name = "dana"
print("hi there %s" % name)
# 当name是一个元组时(1, 2, 3),会抛出类型错误
name = (1, 2, 3)
# print("hi there %s" % name)
# 修改后
print("hi there %s" % (name, ))   # 提供一个单元素的数组而不是一个参数

# 使用.format()函数进行字符串的格式化输出
print("hi there {}".format(name))
