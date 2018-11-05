#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-25 08:57:06
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

"""python字符串拼接总结"""

# 加号拼接
print('hello' + ' world')
# 逗号拼接
print('hello', 'world')
# 直接拼接
print('hello'   'world')
print('hello''world')
# 百分号%
print('%s %s' % ('hello', 'world'))
# format函数
print('{} {}'.format('hello', 'world'))
# join函数
print('-'.join(['aa', 'bb', 'cc']))  # join()函数的参数是一个序列类型，例如列表或元组
print(' '.join(('you', 'are', 'bitch!')))
# f-string
aa = 'hello'
bb = 'world'
print(f'{aa} {bb}')
# 星号*
aa = 'hello '
print(aa * 3)

# 总结：
"""
连接少量字符串时，推荐使用+号操作符
对性能有较高要求，并且python版本在3.6以上，推荐使用f-string
连接大量字符串时，推荐使用join和f-string方式
"""
name = 'curry'
age = 30
gender = 'male'
print('姓名: ' + name + ' 年龄: ' + str(age) + ' 性别: ' + gender)
print(f'姓名: {name} 年龄: {age} 性别: {gender}')
print(' '.join(['I', 'want', 'to', 'fuck', 'you']))
