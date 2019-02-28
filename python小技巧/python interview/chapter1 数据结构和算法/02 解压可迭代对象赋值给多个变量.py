#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-17 10:13:13
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$


# 问题:如果一个可迭代对象中的元素超过变量个数时，会抛出ValueError的错误，那如何才能从这个可迭代对象中解压出N个元素

# 解决方法:python中的*可以解决这个问题


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


# 另外一种情况:假设有一些用户的记录列表，每条记录包含一个名字、邮件、不定数量的号码
record = ("curry", "curry@example.com", "1234567", "847-555-1212")
name, email, *phone_numbers = record
# phone_numbers永远都是list类型,不管解压的电话号码数量是多少
print("phone_numbers =", phone_numbers)
# *也可以用在列表的开始部分
*trailing, current = [10, 4, 5, 78, 4, 30, 5, 9]
print("trailing =", trailing)
print("current =", current)


# 讨论
"""
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象设计的，这些可迭代对象的元素结构有着确定的规则
*可以让开发任意可以很容易的利用这些规则解压出元素来
"""

# *在迭代元素为可变长元组的序列时是很有用的
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# *解压语法在字符串操作时也会很有用，如字符串的分割
line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(":")
print("uname =", uname)
print("fields =", fields)
print("homedir =", homedir)
print("sh =", sh)

# 有时候想解压一些元素后丢弃它们，就不能简单的使用*,可以使用一个普通的废弃名称，如_或ign
record = ('Curry', 30, 91.2, (1992, 10, 30))
name, *_, (*_, day) = record
print("name =", name)
print("day =", day)
"""
在很多函数式语言中，星号解压语法跟列表处理有许多相似之处。比如，如果你有一个列表， 你可以很容易的将它分割成前后两部分
"""
items = [12, 10, 7, 4, 5, 9]
head, *tail = items
print("head =", head)
print("tail =", tail)


def sum_items(items):
    head, *tail = items
    result = head + sum_items(tail) if tail else head   # 递归调用sum_items()函数
    return result


result = sum_items(items)
print(result)
