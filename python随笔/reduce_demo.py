#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
"""reduce()函数介绍"""
# 格式: reduce(function, iterable[, initializer])
def add(x, y):
    return x+y


if __name__ == '__main__':
    t = reduce(add, [1, 2, 3, 4, 5])
    print(t)
    # 使用匿名函数简化
    t = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
    print('使用匿名函数简化:', t)
    sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular.']
    word_count = reduce(lambda a, x: a+x.count("learning"), sentences, 0)
    print('统计learning单词出现的次数:', word_count)