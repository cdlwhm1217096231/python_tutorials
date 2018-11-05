#！/usr/bin/env python3
# -*- coding: utf-8 -*-
"""匿名函数"""
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
# 当传入函数时，有时不需要显示定义简单函数，可以使用匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
import math
t = map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print('返回函数对象: ', t)
t1 = list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(t1)
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
t2 = lambda x: x*x
print('匿名函数也是一个函数对象:', t2)
t3 = t2(5)
print('把匿名函数赋值给一个变量t2，再利用变量t2来调用该函数:', t3)
# 把匿名函数作为返回值返回
def dist(x, y):
    return lambda : math.sqrt(x*x + y*y)

if __name__ == '__main__':
    f1 = dist(2, 3)
    print(f1())

