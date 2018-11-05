#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.6.3
# Tools: Pycharm 2017.3.3

__date__ = '2018/7/19 11:25'
__author__ = 'cdl'
"""python3正则表达式"""

import re

# \d: 表示匹配一个数字  \w：表示匹配一个数字或者字母  .: 可匹配任意字符  *：表示匹配任意个字符  \s : 匹配任意不可见字符 包括空格、制表符、换页符等
# + : 至少匹配一个字符； ？： 表示匹配0或者1个字符  {n}: 表示匹配n个字符  {m,n}： 表示匹配 n-m 个范围的字符
s = '010-12345678'
print(re.match(r'^\d{3}\-\d{3,8}$', s))  # 使用r前缀，不用考虑原字符串中包含的转义字符，成功匹配，返回一个match对象
s = '010 12345678'
print(re.match(r'^\d{3}\-\d{3,8}$', s))
"""
# 常用判断是否匹配成功模板
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
"""
# 切分字符串
s1 = 'a b   c'
print(s1.split(' ')) # 使用空格切分,无法识别连续的空格
# 使用re模块
s2 = 'a   b c      d'
print(re.split(r'\s+', s2))
s3 = 'a,b c   d,e    f'
print(re.split(r'[\s\,]+', s3))
s4 = 'a,b,c;e  f;;,e   g'
print(re.split(r'[\s\,\;]+', s4))
# 分组（）----group()提取子串的功能
s5 = '010-12345678'
m = re.match(r'^(\d{3})-(\d{3,8})$', s5)
print(m.group(0))  # 原始字符串
print(m.group(1))
print(m.group(2))
print(m.groups())
# 贪婪匹配（默认）
m = re.match(r'^(\d+)(0*)$', '102300')
print(m.groups())
# 非贪婪匹配
m = re.match(r'^(\d+?)(0*)$', '102300')
print(m.groups())
# re.compile()预先将字符串编译成正则表达式对象
pattern = re.compile(r'^(\d{3})-(\d{3,8})$')
print(pattern.match('010-12345').groups())

m = re.match(r'^(\w{3,8}).*?(\w{3,8}).*?(\w{3})$', 'someone@gmail.com')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())




