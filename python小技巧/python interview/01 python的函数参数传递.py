#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 09:49:05
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import os


a = 1


def func(a):
    a = 2  # 此时的a是一个局部变量


func(a)   # 调用函数func(a)
print("a:", a)


print('*' * 20)

a = []


def fun(a):
    a.append(1)


fun(a)  # 调用函数fun(a)
print("a:", a)

print("*" * 20)


# 上述函数中，所有的变量都可以理解是对内存中一个对象的"引用"
# 通过id来看引用a的内存地址可以比较理解
a = 1


def fun1(a):
    print("函数内部的变量a的地址:", id(a))
    a = 2
    print("对a重新赋值后的a的地址:", id(a), id(2))


print('函数外部的变量a的地址:', id(a), id(1))
fun1(a)  # 调用函数fun1(a),在执行完a=2后，a引用中保存的值即内存地址
print(a)

print("*" * 20)

a = []


def fun2(a):
    print("函数内部的变量a的地址:", id(a))
    a.append(1)


print("函数外部的变量a的地址:", id(a))
fun2(a)  # 调用函数fun2(a),a引用中保存的内存地址值不会发生变化
print(a)

"""
原因:a = [],定义的一个列表是属于对象，而不是一个变量，对象有两种:可变与不可变对象
不可变对象:string tuple number;可变对象: list dict set
"""
