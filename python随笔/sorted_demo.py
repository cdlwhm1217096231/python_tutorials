#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-17 14:43:34
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""sorted函数"""
# sorted(iterable，key=None,reverse=False)  key接受一个函数，这个函数只接受一个元素，默认为None
students = [('john', 'A', 15), ('Tane', 'B', 12), ('dave', 'C', 10)]
print(type(students))
print(sorted(students, key=lambda x: x[1], reverse=True))
seq = [2, 4, 3, 1, 2, 2, 3]
print(sorted(seq, key=lambda x: seq.count(x)))
print(sorted([False, True]))  # Boolean 的排序会将 False 排在前，True排在后;
# 先比较元组的第一个值，如果相等就比较元组的下一个值，以此类推。
s = 'asdf234GDSdsf23'  # 排序:小写-大写-奇数-偶数
print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))))
list1 = [7, -8, 5, 4, 0, -2, -5]
# 要求1.正数在前负数在后 2.正数从小到大 3.负数从大到小
print(sorted(list1, key=lambda x: (x < 0, abs(x))))  # 先按照正负排序后，再按照大小排序
