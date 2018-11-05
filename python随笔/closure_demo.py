#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 全局变量global
# 如果在函数内部定义一个与全局变量相同名的局部变量，则全局变量会被屏蔽
x = 1
def fun1():
    x = 2
    print("x = ", x)
# 如果要在函数体内部修改全局变量，则要声明函数体内部的变量为全局变量
x = 1
def fun2():
    global x
    print('函数体内部定义的全局变量:x =', x)
    x = 100
    print('此处修改的是全局变量:x = ', x)

# 内嵌函数
# 内嵌函数的作用域只在外部函数的作用域之内，故只能在外部函数的内部调用内嵌函数
def outside():
    print('正在调用外部函数outside...')
#     内嵌函数定义
    def inside():
        print('正在调用内嵌函数inside...')
#     内嵌函数的调用
    inside()
# 内嵌函数与外部函数的关系
def line_config():
    def line(x):
        return 2 * x + 1
    return line   # 外部函数调用内嵌函数line,所以返回函数line

# 修改上述函数定义,给外部函数设置一个局部变量b
def line_config1():
    b = 15
    def line1(x):
        return 2 * x + b
    return line1
# 使用nonlocal关键字
def line_config2():
    b = 20
    def line2(x):
        nonlocal b
        b = 100
        return 2 * x + b
    return line2
# 闭包closure引入
def calc_sum(*args):   # *args可变参数，接收的是一个tuple；关键字参数**kw,接收的是一个dict
    ax = 0
    for n in args:
        ax += n
    return ax
# 如果不需要立刻求和，而是根据需要求和；可以不返回求和结果，返回求和函数.
# 闭包closure-----内部函数引用外部函数的参数和局部变量，外部函数返回内部函数时，相关的参数和变量都保存在返回的函数中。
def calc_sum1(*args):
    def sum1():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum1   # 返回内层函数
# 注意: 返回函数不要引用任何循环变量，或者后续会发生变化的变量;确保引用的局部变量在内部函数返回后不能变
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
# 改进
def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

if __name__ == '__main__':
    fun1()
    fun2()
    # 调用外部函数
    outside()
    # 错误调用内嵌函数
    # inside()
    # 调用外部函数line_config
    my_line = line_config()
    print('调用内嵌函数line:', my_line(5))
    # 调用外部函数line_config1
    b = 5    # 在内部函数line1中只能对外部函数line_config1的局部变量b进行访问，但是不能修改,故b仍为15
    my_line = line_config1()
    print('调用内嵌函数line1:', my_line(5))
    # 在内部函数line1中只能对外部函数line_config1的局部变量b进行访问，但是不能修改,如果要修改使用nonlocal关键字
    my_line = line_config2()
    print('调用内嵌函数line2:', my_line(5))
    sum = calc_sum(1, 2, 3, 4, 5)
    print('sum  = ', sum)
    f1 = calc_sum1(*[1, 2, 3, 4, 5, 6])  # 返回的是求和函数sum1()
    sum1 = f1()  # 调用内部函数sum1()
    print('sum1 = ', sum1)
    # 即使每次传入的参数相同，但返回的函数都不相同
    f2 = calc_sum1(*(1, 2, 3, 4, 5, 6))
    sum2 = f2()
    print('sum2 = ', sum2)
    print('即使每次传入的参数相同，但返回的函数都不相同:', f1 == f2)
    f1, f2, f3 = count()  # 返回的函数引用了变量i,但它并非立刻执行。等到 3个函数都返回时，它们所引用的变量i已经变成了3,因此最终结果为 9
    print('原始:', f1(), f2(), f3())
    fun1, fun2, fun3 = count1()
    print('改进:', fun1(), fun2(), fun3())