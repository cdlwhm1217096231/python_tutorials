#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 09:57:54
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

# 问题引入:现在有一个包含N个元素的元组或序列,怎样将它里面的值解压后同时赋值给N个变量

# 解决方法:任何的可迭代对象,可以通过一个简单的赋值语句解压并赋值给多个变量，前提是变量的数量与序列中的元素个数相同

p = (4, 5)
a, b = p
print("a =", a)
print("b =", b)

data = ["Curry", 30, 91.1, (1992, 10, 10)]
name, age, weight, date = data
print("name =", name)
print("date =", date)
name, age, weight, (year, month, day) = data
print("name =", name)
print("year =", year)
print("month =", month)
print("day =", day)

# 如果变量个数与序列中的元素个数不一致时，会抛出异常
# p = (3, 4)
# x, y, z = p


""" *************************************************************** """
# 总结:上述解压赋值可以用在任何可迭代对象上，不仅仅是列表和元组上，可以是字符串、文件对象、迭代器、生成器
s = "hello"
a, b, c, d, e = s
print("a =", a)
print("b =", b)
print("e =", e)

# 有时候,只想解压一部分数据，丢弃其他值，这时可以使用任意变量名去占位，到时候丢掉这些变量即可
# 必须保证这些占位符变量名在其他地方没有被用到!
data = ["curry", 30, 92.3, (1991, 10, 10)]
_, age, weight, _ = data
print("age =", age)
print("weight= ", weight)
